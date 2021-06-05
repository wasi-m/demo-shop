# Shop App
A simple Category and product structure in Python Django Rest Framework

Users can demoit here http://demo-shopy.herokuapp.com/ and upload the file.


Project Details
--------------------------------------------
- Backend - Python/DjangoRestFramework
- Database - SQLite3 (Not Used)
- Hosted on - Heroku
- website - http://demo-shopy.herokuapp.com/


Setup Project
--------------------------------------------
1. Create a virtual environmnet and activate
```
$ virtualenv venv
$ source venv/bin/activate
```
2. Clone Project from https://github.com/wasi-m/demo-shop.git
```
$ git clone https://github.com/wasi-m/demo-shop.git
```
3. Install all project dependency from requirements.txt file
```
$ pip install -r requirements.txt
```
4. Go to project folder and run the Django makemigrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5. Go to project folder and run Django development server
```
$ python manage.py runserver
```
6. Open http://127.0.0.1:8000 in browser


Future Scope
--------------------------------------------
1. Creating Users for tracking and saving the interests by search.
