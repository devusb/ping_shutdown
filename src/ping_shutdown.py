from time import time,sleep
from ping3 import ping
from sys import argv
from os import system,path,remove
import syslog

def shutdown_countdown(host,wait_time,shutdown_cmd):
    syslog.syslog('shutdown counter commencing...')
    open('/tmp/shutdown_in_progress','a').close()
    start_time = time()

    while True:
        current_time = time()
        elapsed_time = current_time - start_time
        response = ping(host)
        syslog.syslog(str(wait_time - elapsed_time) + " seconds until shutdown")

        if type(response) is float:
            syslog.syslog('ping succeeded! shutdown aborted...')
            remove('/tmp/shutdown_in_progress')
            return

        if elapsed_time > wait_time:
            syslog.syslog('shutting down...')
            remove('/tmp/shutdown_in_progress')
            system(shutdown_cmd)
            return


def main():
    host = argv[1]
    wait_time = int(argv[2])
    shutdown_cmd = argv[3]

    if not path.exists('/tmp/shutdown_in_progress'):
        response = ping(host)

        if response == False or response is None:
            syslog.syslog('initial ping failed...')
            shutdown_countdown(host,wait_time,shutdown_cmd)

        else:
            syslog.syslog('initial ping succeeded!')
    
    else:
        syslog.syslog('shutdown already in progress')

if __name__ == "__main__":
    main()