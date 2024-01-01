#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#when starting a new django project:
#create a new folder
#cd into it and type pypthon -m venv env (this will make a virtual env)
#then type source env/Scripts/activate (this will activate virtual env)
#then type pip install django (this will install django)
#then type django-admin startproject todo_main (this will create a new django project)
#then type python manage.py runserver (this will start the server)
#then type python manage.py migrate (this will create tables in the database)
#then type python manage.py createsuperuser (this will create a superuser)
