#!/usr/bin/env bash

set -e

docker/dirs.sh
if [ "$1" = "web" ]; then
  cp -a media /home/documents/
  python manage.py collectstatic --no-input -c
  python manage.py migrate
  python manage.py reindex_elasticsearch
fi
mkdir -p /run/sshd
/usr/sbin/sshd
gunicorn --error-logfile="-" --timeout=3000  readthedocs.wsgi:application $*
