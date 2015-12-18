#!/bin/bash

######################################################################
# rrd_rest_launcher.sh
# ####################################################################


printandexec () {
		echo "$@"
		eval "$@"
}

printandexec cd /home/user/workspace/OSHI-REST-server
printandexec ./OSHI-REST-server.sh --mode run

