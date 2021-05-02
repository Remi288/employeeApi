# API Service backing client interfaces

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [GithubAction](https://github.com/) : Continuous Integration and Deployment

## Description

 An Api that allows User to create, update and delete employees data

 ## Getting Started

Getting started with this project is very simple, all you need is to have Git installed on your machine. Then open up your terminal and run this command `git clone https://github.com/Remi288/employeeApi.git` to clone the project repository.

Change directory into the project folder `cd EMPLOYEES_Api` 

 At this moment, your project should be up and running with a warning that *you have unapplied migrations*.

Open up another terminal and run this command ` python manage.py makemigrations` for creating new migrations based on the models defined and also run `api python manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```
1. git clone https://github.com/Remi288/employeeApi.git
2. cd EMPLOYEES_Api
3. python manage.py makemigrations
4. python manage.py migrate
```

 ## Setting the Environment Variables
The following setting is in the environment variable

```env
1. SECRET_KEY=
2. JWT_SECRET_KEY=
5. DEBUG=True
```

## Running Tests

```
python manage.py test
```

## SWAGGER Documentation To Test API's

* [Swagger](https://swagger.io/) : Swagger Documentation