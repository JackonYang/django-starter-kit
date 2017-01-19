#!/bin/bash

rm -f db.sqlite3

python manage.py migrate
python manage.py createsuperuser \
    --username=jackon
#    --email=i@jackon.me

python manage.py loaddata default_data/initial_data.json

# rm -rf media
# cp -R init_data media
