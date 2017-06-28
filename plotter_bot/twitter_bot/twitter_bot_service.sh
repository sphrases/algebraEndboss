#!/bin/bash

case "$1" in
start)
   ./hagabot/twitter_bot/ageb.sh &
   echo $!>/var/run/tweet_bot_service.pid
   ;;
stop)
   kill `cat /var/run/tweet_bot_service.pid`
   rm /var/run/tweet_bot_service.pid
   ;;
restart)
   $0 stop
   $0 start
   ;;
status)
   if [ -e /var/run/tweet_bot_service.pid ]; then
      echo twitter_bot_service.sh is running, pid=`cat /var/run/tweet_bot_service.pid`
   else
      echo twitter_bot_service.sh is NOT running
      exit 1
   fi
   ;;
*)
   echo "Usage: $0 {start|stop|status|restart}"
esac

exit 0

