# StatsProject
 Cet projet est une application web basée sur Django conçue pour l'analyse statistique
# Groupe:
## ABDENNACER Elbasri
## AHMED Damou Mohamed
## BILAL Hansali

### Django projet + app:
- pip install django

### Install libraries
- pip install django pandas matplotlib
- pip install lxml

#### Windows: 
- Installer mysql: https://dev.mysql.com/downloads/installer/
#### Linux/ubuntu: 
- sudo apt-get install libmysqlclient-dev
- export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
- export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

#### python mysql client:
- pip install mysqlclient

### Config stats_project/settings.py
- installed_apps: 'stats_app'
- DATABASES = {.. infos.. }

### Definition des models in stats_app/models.py
### Migrations
- python3 manage.py makemigrations
- python3 manage.py migrate

### Forms: stats_app/forms.py
### views stats_app/views.py
### templates stats_app/templates
- upload.html
- result.html

### Update stats_app/urls.py
### Include stats_app/urls.py >> stats_project/urls.py

### Create admin user:
- python3 manage.py createsuperuser
- admin /admin
- default login info (user: stats, pwd: ncr)

### Test:
python manage.py runserver

### Use custom python ENV !