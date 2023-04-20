#!/bin/sh
set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - continuing"

if [ "$DJANGO_MANAGEPY_MIGRATE" = 'on' ]; then
    pipenv run ./manage.py migrate --noinput
fi

if [ "$DJANGO_MANAGEPY_COLLECTSTATIC" = 'on' ]; then
    pipenv run ./manage.py collectstatic --noinput
fi

exec "$@"
