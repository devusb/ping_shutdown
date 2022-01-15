from time import time
from ping3 import ping
from sys import argv
from os import system
import syslog

def shutdown_countdown(host,wait_time):
    print('shutdown counter commencing...')
    start_time = time()

    while True:
        current_time = time()
        elapsed_time = current_time - start_time
        response = ping(host)
        syslog.syslog(str(wait_time - elapsed_time) + " seconds until shutdown")

        if type(response) is float:
            print('ping succeeded! shutdown aborted...')
            return

        if elapsed_time > wait_time:
            print('shutting down...')
            system('poweroff')
            return


def main():
    host = argv[1]
    wait_time = int(argv[2])

    response = ping(host)

    if response == False or response is None:
        print('initial ping failed...')
        shutdown_countdown(host,wait_time)

    else:
        print('initial ping succeeded!')

if __name__ == "__main__":
    main()