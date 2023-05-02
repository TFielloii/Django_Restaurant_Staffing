#!/bin/bash

rm db.sqlite3
rm -Path ".\users\migrations" -Recurse -Include *_initial.py
rm -Path ".\staffing_app\migrations" -Recurse -Include *_initial.py

# Create new database
python manage.py makemigrations
python manage.py migrate

# Populate the Location model with sample data
python manage.py shell << EOF
from staffing_app.models import Location
from users.models import CustomUser
CustomUser.objects.create(email='test@test.test',first_name='test',last_name='mctesty',password='Copious20')
Location.objects.create(name='Alamo Beer', number=1, street_address='123 Rainy St', city='Arlen', state='TX', phone='555-555-5555')
EOF