twly-voter-guide [![Build Status](https://travis-ci.org/g0v/twly-voter-guide.png?branch=master)](https://travis-ci.org/g0v/twly-voter-guide)
================

[立委投票指南](http://vote.ly.g0v.tw/)     

[日本語インストールドキュメント](https://github.com/g0v/twly-voter-guide/blob/master/README.ja.md) - by @nyampire

In Ubuntu 12.04 LTS
=================
0.1 install basic tools
```
sudo apt-get update
sudo apt-get upgrade
sudo reboot
sudo apt-get install git python-pip python-dev python-setuptools postgresql
easy_install virtualenv
```

0.2 set a password in your database(If you already have one, just skip this step)        
(you can use `whoami` to check your username, notice **&lt;username&gt;**  below, please replace with your own)

```
sudo -u <username> psql -c "ALTER USER <username> with encrypted PASSWORD 'put_your_password_here';"
```

## Clone source code from GitHub to local
```
git clone https://github.com/g0v/twly-voter-guide.git       
cd twly-voter-guide
```

## Start virtualenv and install packages         
(if you don' mind packages installed into your local environment, just `pip install -r requirements.txt`)
```
virtualenv --no-site-packages venv      
source venv/bin/activate        
pip install -r requirements.txt     
```

## Restore data into database       
Please new a database(eg. ly), below will use ly for example
```
createdb -h localhost -U <username> ly
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U <username> -d ly local_db.dump
```

## Django settings.py          
create and edit local_settings.py in twly-voter-guide/ly/ to configing your database parameter(notice **USER**, **PASSWORD** below) and **SECRET_KEY**, [sample](https://github.com/g0v/twly-voter-guide/blob/master/ly/local_settings.sample.py)       
See [Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) or maybe use [online generator](http://www.miniwebtool.com/django-secret-key-generator/) to get SECRET_KEY for convenience				
```
SECRET_KEY = '' # put random string inside and don't share it with anybody.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ly', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
```
Because local_settings.py is list in .gitignore, so this file won't be appear in source control, for safety.

## runserver
```
python manage.py runserver
```

## tests(optional)
```
coverage run manage.py test --settings=ly.test
```


For MAC
=================
0.1 install postgresql (use brew)
```
$ brew install postgresql
```
0.2 install pip
```
$ sudo install pip 
```


## git clone
```
git clone https://github.com/g0v/twly-voter-guide.git       
cd twly-voter-guide
```
## install dependent module
```
$ sudo pip install -r requirement.txt
```
(or use virtualenv)

## create db (eg. ly)
```
$ createdb ly
```

## restore data into database       
Please new a database, ex: ly, below will use ly for example
```
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U <username> -d ly local_db.dump
```
you can use `$ whoami` to check your username

## runserver
```
$ python manage.py runserver
```

## tests(optional)
```
$ coverage run manage.py test --settings=ly.test
```

CC0 1.0 Universal
=================
CC0 1.0 Universal       
This work is published from Taiwan.     
[about](http://vote.ly.g0v.tw/about/)
