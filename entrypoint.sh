#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py collectstatic --noinput

cp -rv static/* static_shared/

gunicorn yourapp.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=calendar_api.production_settings \
    --name calendar_api \
    --bind 0.0.0.0:8000 \
    --timeout 600 \
    --workers 4 \
    --log-level=info \
    --reload