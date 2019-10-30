#!/usr/bin/env sh

set -e

echo "Creating empty ES indexes"
docker-compose exec -T web python manage.py search_index --create
