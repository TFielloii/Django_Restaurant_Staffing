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
from staffing_app.models import Location, JobPosting
from users.models import CustomUser

location1 = Location.objects.create(name='Reynholm Industries', address='123 Carenden Rd', city='London', state='England')
location2 = Location.objects.create(name='Strickland Propane', address='123 Rainy St', city='Arlen', state='TX')

CustomUser.objects.create(email='test@test.test',first_name='John',last_name='Smith',password=make_password('password1'))
man = CustomUser.objects.create(email='man@man.man',first_name='Hank',last_name='Hill',password=make_password('password1'), is_hiring_manager=True, location=location1)
man.location = location2
man.save()
admin = CustomUser.objects.create(email='admin@admin.admin',first_name='Buck',last_name='Strickland',password=make_password('password1'), is_restaurant_administrator=True, location=location2)
admin.location = location2
admin.save()
man2 = CustomUser.objects.create(email='man2@man.man',first_name='Maurice',last_name='Moss',password=make_password('password1'), is_hiring_manager=True, location=location1)
man2.location = location1
man2.save()
admin2 = CustomUser.objects.create(email='admin2@admin.admin',first_name='Douglas',last_name='Reynholm',password=make_password('password1'), is_restaurant_administrator=True, location=location1)
admin2.location = location1
admin2.save()

JobPosting.objects.create(title='IT Goblin', location=location1, descr='IT stuff.', requirements='Doing IT stuff.', salary='1.50')
JobPosting.objects.create(title='Chef', location=location2, descr='Chef stuff.', requirements='Doing Chef stuff.', salary='12.50')

EOF