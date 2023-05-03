# Django_Restaurant_Staffing

This is the repository of Thomas Fiello's internship project for ExpandShare (Summer 2023).

## Getting Started

### Setting up environment
First, I recommend to create an environment to install the appropriate Python packages. For this I recommend using virtualenv (venv) as it is already setup for it.

Inside the repository is a bin folder with a setup_env.sh file which contains all necessary packages to execute the code. The environment including the packages can be created and installed by executing the following command: 
```console
bash bin/setup_env.sh
``` 

This will automatically create and start the environment, as well as install any required modules from the requirements.txt file.

### Start the local server
Once you have everything installed and ready, start the local server by entering the following command:
```console
python manage.py runserver
``` 

## File Details

### Django_Restaurant_Staffing
This is the main project folder and contains the sensitive information like settings.py. Other than that it acts as a common connection for the apps.

### staffing_app
This holds all of the models, templates, views, urls, etc for any of the database information.

### users
This holds all of the models, templates, views, urls, etc for any of the user and authentication information.

## Disclaimer
The code and these instructions were tested using Python 3.8.8 and Windwos 10. Depending on your operating system modifications might be needed. Feel free to contact us in case any problems occure or questions arise.