.. image:: https://travis-ci.org/Azelphur-Servers/django-game-info.svg?branch=master
    :target: https://travis-ci.org/Azelphur-Servers/django-game-info
.. image:: https://coveralls.io/repos/Azelphur-Servers/django-game-info/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/Azelphur-Servers/django-game-info?branch=master 
.. image:: https://requires.io/github/Azelphur-Servers/django-game-info/requirements.svg?branch=master
     :target: https://requires.io/github/Azelphur-Servers/django-game-info/requirements/?branch=master
     :alt: Requirements Status
=====
django_game_info
=====

django_game_info is a Django app to collect data from game servers
that respond to the A2S protocol defined at https://developer.valvesoftware.com/wiki/Server_queries
Examples of servers that follow this protocol include::

- Team Fortress 2
- Counter Strike: Source
- Counter Strike: Global Offensive

the module provides a json feed which you can use to display lots
of information about your servers, perfect to put in your sites
sidebar.

Quick start
-----------

1. Install with `pip install django-game-info`

2. Add "game_info" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'game_info',
    ]

3. Include the game_info URLconf in your project urls.py like this

    url(r'^game_info/', include('game_info.urls')),

4. Run `python manage.py migrate` to create the models

5. Start the development server and visit http://127.0.0.1:8000/admin
   to add some servers (you'll need the Admin app enabled)

6. Run `python manage.py update_game_info` to gather information from
   your game server(s)

7. Visit http://127.0.0.1:8000/game_info/ to see a JSON feed of the
   gathered information
