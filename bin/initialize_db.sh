#!/bin/bash

rm db.sqlite3
rm -Path ".\users\migrations" -Recurse -Include *_initial.py
rm -Path ".\staffing_app\migrations" -Recurse -Include *_initial.py

# Create new database
python manage.py makemigrations
python manage.py migrate

# Populate the Location model with sample data
python manage.py shell << EOF
from django.contrib.auth.hashers import make_password
from staffing_app.models import Location
from users.models import CustomUser
location = Location.objects.create(name='Alamo Beer', address='123 Rainy St', city='Arlen', state='TX')
CustomUser.objects.create(email='test@test.test',first_name='test',last_name='test',password=make_password('Copious20'))
man = CustomUser.objects.create(email='man@man.man',first_name='man',last_name='man',password=make_password('Copious20'), is_hiring_manager=True)
man.location = location
man.save()
admin = CustomUser.objects.create(email='admin@admin.admin',first_name='admin',last_name='admin',password=make_password('Copious20'), is_restaurant_administrator=True)
admin.location = location
admin.save()
EOF