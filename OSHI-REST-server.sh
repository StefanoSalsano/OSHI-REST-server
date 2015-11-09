#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

while [[ $# > 1 ]]
do
key="$1"

case $key in
    -m|--mode)
    MODE="$2"
    shift # past argument
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done

if [ -z ${MODE+x} ]
	then
		echo "MODE is unset. Set it with -m or --mode. Available options are: setup, run. This script will now terminate."
		exit 1
fi

if [[ ${MODE} = 'setup' ]]
	then
	  echo "Setting up environment..."
	  apt-get install rrdtool librrds-perl librrd-dev
	  pip install rrdtool
	  pip install Django
      pip install djangorestframework
      pip install markdown
      pip install django-filter
      pip install pyrrd
      pip install django-rest-swagger
elif [[ ${MODE} = 'run' ]]
	then
	  echo "Running REST server"
	  cd /home/user/workspace/OSHI-REST-server/oshi_rest_server
	  ./manage.py runserver
fi