#!/bin/ash

echo "Apply migration"
python manage.py migrate

exec "$@"