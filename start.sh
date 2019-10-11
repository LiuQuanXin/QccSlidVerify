#!/usr/bin/env bash

ps -ef|grep Server/servers.py |awk '{print $2}'|xargs kill -9
nohup python Server/servers.py  2>&1 >> log/log.err   &

ps -ef|grep qcc_new.py |awk '{print $2}'|xargs kill -9
ps -ef|grep firefox |awk '{print $2}'|xargs kill -9
ps -ef|grep geckodriver |awk '{print $2}'|xargs kill -9
ps -ef|grep phantomjs |awk '{print $2}'|xargs kill -9
ps -ef|grep 1920x1080x24 |awk '{print $2}'|xargs kill -9
n=0
while ((n>1))
    do
        nohup python spider/qcc_new.py 2>&1 >> log/log.err   &
        let n--
    done


