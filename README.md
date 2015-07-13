# ttghelper

This is a django/postgres fueled app designed to help game masters store and manage session information.

Users create campaigns wtih can store characters, sessions, and notes. Characters and sessions can in turn store notes.

To use offline:
	1) Clone to desktop

	2) Install Django, PostgreSQL, psycopg2

	3) sudo -u postgres createuser -s admin

	4) createdb -U admin --locale=en_US.utf-8 -E utf-8 -O admin db.sessions -T template0

	5) python manage.py makemigrations

	6) python manage.py migrate

	7) python manage.py runserver

	8) go to localhost:8000/sessions


sw.wookscrapper(string article):
	Take a string and return the summary of the wookiepedia article by that name to the command line. When given no argument, user will be prompted.
  
