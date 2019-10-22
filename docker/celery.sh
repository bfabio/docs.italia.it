#!/usr/bin/env bash

set -e

docker/dirs.sh

mkdir -p ${HOME}/.ssh && ssh-keyscan -H ${APP_HOSTS} >> ${HOME}/.ssh/known_hosts
celery worker ${*:2}
