#!/bin/bash
daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
# As if,open new shell and run (exec sh  "$0")
exec echo "Finally Daemon, System can be run systemctl!"
exec nsenter -t $(pidof systemd) -a su - $LOGNAME
# Init modules and echo "System can be run systemctl!"
systemctl daemon-reload
exit 1
