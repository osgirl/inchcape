Description of project:

Getting started:
# # Uses postgres
# sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
# # Get the database setup
# sudo su - postgres
# psql
# CREATE DATABASE inchcape;
# # Double check that you built the database
# \l
# CREATE USER k WITH PASSWORD 'password';
# ALTER ROLE k SET client_encoding TO 'utf8';
# ALTER ROLE k SET default_transaction_isolation TO 'read committed';
# ALTER ROLE k SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE inchcape TO k;
# # Exit the database admin
# \q
# exit

# # Uses pip and virtualenv
# sudo apt-get install pip
# sudo pip install virtualenv
# virtualenv -p /usr/bin/python3.4 ufw # Makes a virtual environment with the correct python version
# # activate the inchcape virtual environment
# source inchcape/bin/activate

# # Download the code
# git clone https://github.com/k-mad/inchcape.git
# # install requirements
# pip install -r requirements.txt

# # Hook up the database
# python manage.py makemigrations
# python manage.py migrate
# # should be ready to go.

# # Make an admin user.
# python manage.py createsuperuser

# # Backup the database with fixture
# python manage.py dumpdata --format=json --indent=4 > inchcape/apps/app_name/fixtures/fixture_name.json
# # Restore the database from json fixture
# python manage.py migrate app_name zero
# python manage.py migrate
# python manage.py loaddata fixuture_name.json

# # Make a new app
# python manage.py startapp new_app_name
# mv new_app_name inchcape/apps/

# # Delete a table in the database
# sudo su - postgres
# psql

# # Show databases
# sudo su - postgres
# psql
# \l

# # Delete a database
# sudo su - postgres
# psql
# DROP DATABASE inchcape;

