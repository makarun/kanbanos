# kanbanos
Simple ToDo App with Django & PostgreSQL
## Done:
* views
* login
* task edit
* task remove
* stage model / add / remove / change status

## To Do:
* multiple user acces to task
* stages edit
* stages sorting
* name of task on add_stage view
* adding filles to task

### history/silva rerum:

	making virtual env:
		virtualenv --python=python3.5 myvenv
		source myvenv/bin/activate
	installing django:
		pip install django
	installing postgresql:
		sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
		https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
	creating database:
		CREATE DATABASE kanbanos
	adding user:
		CREATE USER kanbanosuser WITH PASSWORD 'password';
	changing settings:
		ALTER ROLE kanbanosuser SET client_encoding TO 'utf8';
		ALTER ROLE kanbanosuser SET default_transaction_isolation TO 'read committed';
		ALTER ROLE kanbanosuser SET timezone TO 'UTC';
	adding priviliges:
		GRANT ALL PRIVILEGES ON DATABASE kanbanos TO kanbanosuser;
	installing psycopg2:
		pip install psycopg2
	project initialization:
		django-admin.py startproject kanbanos .
	kanbanos/settings.py:
		DATABASES = {
 				default': {
					'ENGINE': 'django.db.backends.postgresql_psycopg2',
					'NAME': 'myproject',
					'USER': 'myprojectuser',
					'PASSWORD': 'password',
					'HOST': 'localhost',
					'PORT': '',
				}
		}'
	admin:
		python manage.py createsuperuser
	test:
		python manage.py runserver
	starting app:
		python manage.py startapp todo
	kanbanos/urls.py:
		url(r'^todo/', include('todo.urls')),
	todo/urls.py:
		url(r'^$', views.index, name='index'),
	making models at todo/models.py
		python manage.py makemigrations todo
		python manage.py migrate todo
	todo/admin.py
		from django.contrib import admin
		from .models import Task
		admin.site.register(Task)
	views
		base
		task_add
		task_detail
		task_list
	login
	task edit
	task remove
	views
		task_aborted_list
		task_doing_list
		task_done_list
		task_todo_list
	stage model
	stage add view
		add_stage_to_task
	stage remove
	stage change status

###ToDo:

	stages edit
	stages sorting
	name of task on add_stage view

