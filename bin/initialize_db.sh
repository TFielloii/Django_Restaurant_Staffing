#!/bin/bash

# Remove old database and migration files
rm db.sqlite3
rm -rf "./users/migrations/*_initial.py"
rm -rf "./staffing_app/migrations/*_initial.py"

# Create new migrations and apply them to the database
python manage.py makemigrations
python manage.py migrate

# Populate the Location model with sample data

python manage.py shell << EOF

# Import necessary modules
from django.contrib.auth.hashers import make_password
from staffing_app.models import Location, JobPosting, Restaurant
from users.models import CustomUser

# Create sample Restaurants
restaurant1 = Restaurant.objects.create(name='Strickland Propane')

restaurant2 = Restaurant.objects.create(name='Reynholm Industries')

# Create sample locations
location1 = Location.objects.create(address='123 Rainy St', city='Arlen', state='TX', restaurant=restaurant1)

location2 = Location.objects.create(address='123 Carenden Rd', city='Central London', state='London', restaurant=restaurant2)

location3 = Location.objects.create(address='Broom Rd', city='Teddington', state='London', restaurant=restaurant2)

# Create sample users
CustomUser.objects.create(email='test@test.test', first_name='John', last_name='Smith', password=make_password('password1'))

CustomUser.objects.create(email='man@man.man', first_name='Hank', last_name='Hill', password=make_password('password1'), is_hiring_manager=True, location=location1)

CustomUser.objects.create(email='man2@man.man', first_name='Maurice', last_name='Moss', password=make_password('password1'), is_hiring_manager=True, location=location2)

CustomUser.objects.create(email='man3@man.man', first_name='Roy', last_name='Tenneman', password=make_password('password1'), is_hiring_manager=True, location=location3)

CustomUser.objects.create(email='admin@admin.admin', first_name='Buck', last_name='Strickland', password=make_password('password1'), is_restaurant_administrator=True, restaurant=restaurant1)

CustomUser.objects.create(email='admin2@admin.admin', first_name='Douglas', last_name='Reynholm', password=make_password('password1'), is_restaurant_administrator=True, restaurant=restaurant2)

# Create sample job postings
JobPosting.objects.create(title='Jr Grill Associate', location=location1, description='Floor salesman.', requirements='Must be able to sell propane and propane accessories.', salary='12.50')

JobPosting.objects.create(title='IT Goblin', location=location2, description='Code monkey.', requirements='Must know how to turn it off and back on again.', salary='1.50')

JobPosting.objects.create(title='CEO', location=location3, description='The boss. Head honcho. Numero Uno.', requirements='Must know how to delete the pension account.', salary='999999.99')

EOF