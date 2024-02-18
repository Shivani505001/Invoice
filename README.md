# Invoice
A basic Invoice application using django rest framework. 

## Getting Started 
Create a virtual environment: `python -m venv venv`
Installations: 
- Make sure to have a latest pip version
- To install django  `pip install django`
- For restframework `pip install djangorestframework`

Create a new project : `django-admin startproject project_name`

Create a new app: `python manage.py startapp app_name`

Add the app_name and restframework in 'Installed_apps' in settings.py 

INSTALLED_APPS = [

    ...
    'rest_framework',
    'app_name',
    
],

## Invoice application 
This application is mainly about API generation using django restframework. There are two api endpoints :
- `/invoices/` -- this contains all invoices details 
- `/invoices/<id>` -- this contains sepcific invoice details based on user id.

## Scope of improvement
- Can make a frontend application using django templates or java script.
- Can add pdf feature for each invoice
- Add emailing feature to send the invoice pdf for specifi user.
