#!/bin/bash
#
# Napisati bash skript koji omogucava korisniku da pozove jedan od cetiri signala
# nad procesom zadatim sa pid-om. Signal koji se salje procesu i pid procesa se 
# prosledjuju kao argumenti komandne linije. Signali koje treba podrzati su
# SIGSTOP (kod 19), SIGKILL (kod 9), SIGTERM (kod 15) i SIGCONT (kod 18).
# 
# Argumenti:
#   $1 - signal
#   $2 - PID procesa kojem se salje signal
#
# Primer poziva:
#   ./04_kill_process.sh STOP <pid-procesa>


# TODO implementirati
signal=$1
pid=$2

case $signal in
        STOP)
        echo "Signal SIGSTOP"
        kill -19 $pid ;;
        KILL) 
        echo "Signal SIGKILL" 
        kill -9 $pid ;;
        TERMINATE) 
        echo "Signal SIGTERM"
        kill -15 $pid ;;
        CONTINUE) 
        echo "Signal CONTINUE"
        kill -18 $pid ;;
        *) echo "Nepoznata naredba"
esac

