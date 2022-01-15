# ping_shutdown
Shutdown host when remote host unavailable

Intended use case is to run as part of a cronjob -- example syntax to run every minute, and wait 10 minutes after failed ping for shutdown:
```
*/1 * * * * /usr/bin/python3 ping_shutdown.py 192.168.99.1 600 /sbin/poweroff
```