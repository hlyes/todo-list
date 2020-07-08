# todo-list
Ceci est un projet d'entrainement sur le framework Django (python3) pour l'écriture d'une app web pour l'edition de todo lists simples

# Before doing anything
You should make sure that you have python (ideally version 3.8 and further) and install django.

To install python and  some setup tools
    
    sudo apt install python3.8 python-setuptools python3-pip 
    pip install virtualenv

Once pip3 is installed, you can make sure to use it as your default pip by adding the following line to your ~/.bashrc  (or ~/.bash_profile) file

    alias pip="pip3"

# First baby steps of a django project
In order to start the development of a django project you'd better set your environment and start it

    virtualenv venv -p python3.8 # to make sure to pickup python3.8
    source venv/bin/activate # . venv/bin/activate works only with bash
    pip install django

Once installed you're now able to  use django to create your projects, for example:

    django-admin.py startproject PROJECT_NAME

Inside your project, you can create sub apps using

    ./manage.py startapp APP_NAME

In order to make an app taken into consideration by Django Framework you should go to your project settings and add it to `INSTALLED_APPLICATION` variable. For example:
 
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "todoList", # << an app that has been added
    ]
# From model to DB
## Generate migrations
Once your models defined or updated, you may generate the migrations that will be performed on your database by using 

    ./manage.py makemigrations

It will then generate the migrations for all the installed apps of your project. However, you can generate migrations to only one app. For example:

    ./manage.py makemigrations todoList

Will generate migrations for `todoList` app only.

## Apply migrations

One command is enough to perform this action 

    ./manage.py migrate 

As for `makemigrations` command, you can also perform command by specifying an app or a specific migration (No need to go further now ;-) )


# First run

Once all the steps above performed you are now able to run your django project. To do so:

    ./manage.py runserver

If you test on other computers on the same network you'd better run 

    ./manage.py runserver 0.0.0.0:8000 

to open your server for requests coming from other hosts.

 ... to be continued