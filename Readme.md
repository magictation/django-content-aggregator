A starter for content aggregator build with Django. It has starter models, utilizes SQL database build in Django. Uses [feedparser](https://pypi.org/project/feedparser/) and [django-apscheduler](https://pypi.org/project/django-apscheduler/) libraries. For timestamps 

##**Django**
```
$ python manage.py createsuperuser
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py runserver

$python manage.py startjobs - start django scheduler commands for podcasts, described in podcasts/managemeng/commands
```

##**Pipenv**
Create a environment for python packages
```
pipenv shell
```
If you need to change or add dependencies do:
```
pipenv lock -r > requirements.txt - creating requrements.txt
```