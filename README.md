# DjangoBlog


A blog system based on `python3.8` and `Django3.0`.

[![Requirements Status](https://requires.io/github/liangliangyy/DjangoBlog/requirements.svg?branch=master)](https://requires.io/github/liangliangyy/DjangoBlog/requirements/?branch=master)  

## Main Features:
- All Auth features Login, Logout, Register, Verify User, Password Forgot.
- User is allowed to do CRUD operations on blog-post.

## Installation

1. Clone project to your computer using git, or just download.
2. Open terminal or cmd and go to file location where project cloned.
3. Use the requirements file to get all dependencies.
4. Install via pip: `pip install -r requirements.txt`.

### Configuration
Most configurations are in `setting.py`, others are in backend configurations.

I set many `setting` configuration with my environment variables (such as: `SECRET_KEY`, `SENDGRID_kEY`, and some email configuration parts.) and they did NOT been submitted to the `GitHub`. You can change these in the code with your own configuration or just add them into your environment variables.

More deploy detail in this article.

## Run

Modify `my_Blog/setting.py` with database settings, as following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'django_admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Create database
Run the following command in PostgreSQL shell:

```sql
CREATE DATABASE myproject; 
CREATE USER django_admin WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO django_admin;
```

Run the following commands in Terminal:
```bash
./manage.py makemigrations
./manage.py migrate
```

**Attention: ** Before you using `./manage.py`, make sure the `python` command in your system is towards to `python 3.6` or above version. Otherwise you may solve this by one of the two following methods:
- Modify the first line in `manage.py`, change `#!/usr/bin/env python` to `#!/usr/bin/env python3`
- Just run with: `python3 ./manage.py makemigrations`

### Create super user

Run command in terminal:
```bash
./manage.py createsuperuser
```

### Getting start to run server
Execute: `./manage.py runserver`

Open up a browser and visit: http://127.0.0.1:8000/ , the you will see the blog.


