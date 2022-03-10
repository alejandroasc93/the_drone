# the_drone

System Requirements
-

- python >= 3.9
- redis >= 3.2

Build
-
Install requirements
> pip install -r requirements.txt

Django migrate
> python manage.py migrate
 ````
NOTE:
The database used is sqlite. The project database will be created automaticly in project root.
````

Load data
> python manage.py load_data

Run periodic task

- Terminal 1

> celery -A the_drone worker -P solo --loglevel=info

- Terminal 2

> celery -A the_drone beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

Run
-
> python manage.py runserver

Test
-
Run test command
> python manage.py test

````
Located in directory tests/collection/drone.postman_collection.json are a postman collection file. 
This collection can be loaded in to postman app or web to do api tests. In this collection are one api example for each endpoint.
````

API URL
-
- {server}/api/drone/create/
- {server}/api/drone/load-medication/
- {server}/api/drone/checking-loaded/1/
- {server}/api/drone/checking-available
- {server}/api/drone/checking-available
- {server}/api/drone/checking-battery-level/1
