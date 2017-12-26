#!/bin/bash
set -e
#LOGFILE=/home/ubuntu/uniquesols/pcs_server.log
#LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=ubuntu
TIMEOUT=15
cd /home/ubuntu/uniquesols/
source /home/ubuntu/.virtualenvs/django1.10/bin/activate
gunicorn -b "0.0.0.0:8080" --timeout $TIMEOUT \
--log-level debug \
--user=$USER \
--worker-class gevent -w $NUM_WORKERS uniquesols.wsgi:application
