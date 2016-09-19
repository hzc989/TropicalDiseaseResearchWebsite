#!/bin/bash

ACTION=${1}

start(){
    nohup python ./manage.py runserver --host 0.0.0.0 -p 5000 &
}

stop(){
    pid=$(ps aux | grep runserve[r] | awk {'print $2'})
    kill -9 ${pid}
}

help(){
    echo "${0} start|stop|restart"
}
case ${ACTION} in
"start")
    start
    ;;
"stop")
    stop
    ;;
"restart")
    stop
    start
    ;;
*)
    help;;
esac
