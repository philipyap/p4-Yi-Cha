# Yi-Cha e-commerce app
## Introduction
This is an online ordering app developed in Django-3. Yi-Cha is a place for all tea lovers ! Yi-Cha means Japanese tea ceremony and it's ART of tea! Beyond just serving and receiving tea, one of the main purposes of the tea ceremony is for the guests to enjoy the hospitality of the host in an atmosphere distinct from the fast pace of everyday life. MAKE SURE you sign-up and log-in to shop around our app! Feel free to visit our site : [Welcome to Yi-Cha](https://yicha.herokuapp.com/)

## Technologies Used
- Django Framework, Python3
- PostGreSQL 
- HTML, Javascript
- CSS, Bootstrap 4.5

## User Stories
- User can view: menu, item list in shopping cart, and user profile info.
- User must login to access shopping cart and history details.
- User can create/edit items in shopping cart.
- User can create/edit own profile info.
- User can update or delete items in shopping cart brefore confirmation order.
- User can pay by Paypal once order confirmed. 
- Users able to check or delete their order history in profile page.

## Installation Instructions
1. Fork and clone the repository.
2. Setup virtual environment by:
```
    - pipenv shell
    - pipenv install django==3.0
```
3. Install requirements by:
```
    - cd requirements.txt
    - pip install -r requirements.txt
```
4. Add a .env file with SECRET_KEY set up.
5. Migrate Database
```
    - python3 manage.py makemigration
    - python3 manage.py migrate
```
6. Create Superuser
```
    - python3 manage.py createsuperuser
```
7. Run Server
```
    - python3 manage.py runserver
    goto browser : localhost:8000
```
8. Run Admin Site (superuser)
```
    localhost:8000/admin
```

## Website Pages

## Wireframes

## ERD
![ERD](./main_app/static/images/ERDP4.png)



## Major hurdles of this app

## CRUD