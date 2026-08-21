#!/bin/bash

JDBC_DRIVER=/opt/IBM/jdbc/db2jcc4.jar

if hash rlwrap; then
    # uses rlwrap for wsadmin, so you have history function within wsadmin
    # see http://www.stoeps.de/command-history-wsadmin-on-linux/
    rlwrap -r ./wsadmin.sh $@ -javaoption -Dcom.ibm.ws.scripting.classpath=${JDBC_DRIVER}
else
    ./wsadmin.sh $@ -javaoption -Dcom.ibm.ws.scripting.classpath=${JDBC_DRIVER}
fi
