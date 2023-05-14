# Django_Restaurant_Staffing

This is the repository of Thomas Fiello's internship project for ExpandShare (Summer 2023).

## Getting Started

### Setting up environment
From the main directory, I recommend creating an environment for installing the appropriate Python packages.

Inside the bin folder is a setup_env.sh file which will automatically create and start the venv environment, as well as pip install any required modules from the requirements.txt file. Run it by executing the following command: 
```console
bash bin/setup_env.sh
. /venv/Scripts/Activate
``` 

### Create initialized environment
Once the virtual environment is established, you can skip to creating the different locations, users, jobs, and superusers yourself, or, in the same bin folder as the previous step, there is an initialize_db.sh file which is setup to create the samples listed below. To ensure that there are no conflicting database issues, when this code is executed, it will also automatically remove the current db.sqlite3 file as well as any migrations currently found in the two apps. To run the file, execute the following command:
```console
bash bin/initialize_db.sh
```

Sample restaurants:
| Locations  |         Name        |
|------------|---------------------|
| Restaurant 1 | Strickland Propane  |
| Restaurant 2 | Reynholm Industries |

Sample locations:
| Locations  |    Address    |      City    |     State     |     Restaurant     |
|------------|---------------|--------------|---------------|--------------------|
| Location 1 | 123 Rainy St  | Arlen | TX | Strickland Propane  |
| Location 2 | 123 Carenden Rd | Central London | London | Reynholm Industries |
| Location 3 | Broom Rd | Teddington | London | Reynholm Industries |

Sample users:
| User Type  | Location/Restaurant  |    Email    |  Password  |
|------------|------------|-------------|------------|
|Base User| NA |test@test.test|password1|
|Hiring Manager| Location 1 | man@man.man |password1|
|Hiring Manager| Location 2 | man2@man.man |password1|
|Hiring Manager| Location 3 | man3@man.man |password1|
|Rest Admin| Restaurant 1 | admin@admin.admin |password1|
|Rest Admin| Restaurant 2 | admin2@admin.admin |password1|

Sample job postings:
| Job Title  |      Locations |
|------------|----------------|
|Jr Grill Associate| Location 1 |
|IT Goblin| Location 2  |
|CEO| Location 3  |

If you want to create more restaurant administrators or hiring managers you must create a superuser with the following command:
```console
python manage.py createsuperuser
```

## Start the local server
You are now ready to start the local server with the following command:
```console
python manage.py runserver
```

### Testing email server
Inside the project folder ./Django_Restaurant_Staffing/settings.py file you can find the email settings. Change the EMAIL_HOST_USER to whatever your desired email address is (currently setup for gmail) and then you can create a file in the main directory called 'django_gmail_pass.txt' to store the Google generated APP password.

### Accessing the API directory
To access the API directory. Just add /api/ to the end of the URL's homepage. For example:
If your website is the local server, then the APIs would be located at http://127.0.0.1:8000/api/

## File Details

### Django_Restaurant_Staffing
This is the main project folder.

### staffing_app
This app holds all of the models, templates, views, urls, etc for the locations, job postings, and applications.

### users
This app holds all of the models, templates, views, urls, etc for any of the user personas and authentication.

## Disclaimer
The code was all tested using Django 4.2.1, Python 3.8.8, and a virtual environment inside Windows 10. Depending on your operating system, modifications may be needed. Feel free to contact me with any questions, recommendations, or concerns at tfielloii@yahoo.com