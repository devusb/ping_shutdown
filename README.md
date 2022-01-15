# ping_shutdown
Shutdown host when remote host unavailable

Intended use case is to run as part of a cronjob -- example syntax to run every 10 minutes, and wait 30 seconds after failed ping for shutdown:
```
*/10 * * * * /usr/bin/python3 /root/ping_shutdown.py 192.168.99.1 30
```