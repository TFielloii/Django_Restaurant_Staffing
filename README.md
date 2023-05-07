# Django_Restaurant_Staffing

This is the repository of Thomas Fiello's internship project for ExpandShare (Summer 2023).

## Getting Started

### Setting up environment
From the root directory, I recommend creating an environment to install the appropriate Python packages, such as virtualenv (venv) as it is already setup for it.

Inside the repository is a bin folder with a setup_env.sh file which contains all necessary packages to execute the code. The environment including the packages can be created and installed by executing the following command: 
```console
bash bin/setup_env.sh
. /venv/Scripts/Activate
``` 

This will automatically create and start the environment, as well as install any required modules from the requirements.txt file.

### Create initialized environment
This will create a sample for every user type, sample locations, and a job posting, described below:
```console
bash bin/initialize_db.sh
```

It creates the following locations:
| Locations  |         Name        |
|------------|---------------------|
| Location 1 | Strickland Propane  |
| Location 2 | Reynholm Industries |


The following users:
| User Type  | Locations  |    Email    |  Password  |
|------------|------------|-------------|------------|
|Base User| NA |test@test.test|password1|
|Hiring Manager| Location 1 | man@man.man |password1|
|Hiring Manager| Location 2 | man2@man.man |password1|
|Rest Admin| Location 1 | admin@admin.admin |password1|
|Rest Admin| Location 2 | admin2@admin.admin |password1|


The following job postings:
| Job Title  |      Locations |
|------------|----------------|
|Jr Grill Associate| Location 1 |
|IT Goblin| Location 2  |

If you want to create more restaurant administrators or hiring managers you must create a super user with the following command:
```console
python manage.py createsuperuser
```

### Start the local server
Once you have everything installed and ready, start the local server by entering the following command:
```console
python manage.py runserver
```

### Testing email server
Inside the project folder Django_Restaurant_Staffing/settings.py file you can find the email settings. The 

### Create initialized environment
To access the API directory. Just add /api/ to the end of the URL's homepage. For example:
If your website is the local server, then the APIs would be located at http://127.0.0.1:8000/api/

## File Details

### Django_Restaurant_Staffing
This is the main project folder.

### staffing_app
This holds all of the models, templates, views, urls, etc for the locations, job postings, and applications.

### users
This holds all of the models, templates, views, urls, etc for any of the user personas and authentication information.

## Disclaimer
The code and these instructions were tested using Python 3.8.8 and Windows 10. Depending on your operating system modifications might be needed. Feel free to contact us in case any problems occure or questions arise.
