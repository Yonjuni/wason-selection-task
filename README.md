Wason selection task
====================

Wason selection task is a browser application to perform the Wason selection task. A set of cards is displayed to the user with a statement regarding those cards. The user has to prove the statement by selecting cards that should be flipped. By the cards the user turned it can be unterstood whether the user unterstood the previous statement.

Task Types
----------

There are two types of tasks: abstact and concrete tasks, where abstract ones are refering to numbers and letters and concrete ones contain a story.

Requirements
------------

* Python 2.7
* Django 1.6

Installation
------------

There are two options of hosting the application: With or without virtualenv 

If you intend to use virtualvenv, navigate to your desired directory and start by: 

    virtualenv venv
    source venv/bin/activate

On a production server this probably is located somewhere in /var/www , on a developers computer this normally is located somewhere in your $HOME.

Now you can clone the sourcecode of the application into your directory:

    git@github.com:Yonjuni/wason-selection-task.git

After that you should have a subdirectory wason-selection-task/ and if you created a virtualenv also a subdirectory venv/. The actual application is in the wason-selection-task/ directory. Please navigate into the wason-selection-task directory. 

The application itself is done, but you need to initialize your database. You can canfigure wason-selection-task/settings.py to use mySQL or PostGreSQL described here. Or you can leave the file as it is to use sqlite. The default language is Japanese, so please also change LANGUAGE_CODE to your desired language.

Initialize your database with

    ./manage.py syncdb
    
If you would like to add initial task data for testing or whatever you can do this by

    ./manage.py initial_data

Sample data can be found in intial_data.json file in the Wason_Selection_Task directory (or however you named it), it is written in Jason format and can of course be changed. 
    
Start a development Server
--------------------------
If you intend to make some changes, you can start the application now with

    ./manage.py runserver
    
The application can be accessed under the url `http://localhost:8000`.

Deployment on a production server
---------------------------------
On a production server you should change these settings as they might expose information about
your server to possible attackers.

Edit `wason-selection-task/settings.py` and change `DEBUG` and `TEMPLATE_DEBUG` to `False`. In `settings.py` is a [link](https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/) to the Django documentation with tips for 
what to do on production servers.

There is wsgi file (`wason-selection-task/wsgi.py`) which you can use with a wsgi-server like 
[uwsgi](https://uwsgi-docs.readthedocs.org/en/latest/ "uwsgi website and documentation"). As this is dependant on
which webserver you use please refer to the documentation of your wsgi and webserver of your choice. We successfully 
tested this with uwsgi and nginx.

Further explanation
-------------------
For further explanation see the [Wiki on Github](https://github.com/Yonjuni/wason-selection-task/wiki "Wiki on Github").
