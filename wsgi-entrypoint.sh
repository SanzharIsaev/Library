#!/bin/sh

until cd /config
do
  echo 'Waiting'
done

until ./my_library/manage.py makemigrations
      ./my_library/manage.py migrate
do
  echo 'Waiting DB'
  sleep 2
done

./my_library/manage.py collectstatic --noinput

gunicorn config.wsgi --bind 0.0.0.0:8080 --workers 4 --threads 4