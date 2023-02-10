# My Blog

My blog is simple neat and clean blog site built with Django, HTMX, and Bootstrap 5.

#### Download:
```
git clone https://github.com/4yub1k/djblog.git
cd djblog
```

#### Setup Env:
```
python -m venv .venv
```
#### Activate Env:
```
.venv\Scripts\activate
```

#### Install Requirements:
Make sure Virtual Environment is enabled/activated
```
pip install -r requirements.txt
```

#### Set Environment Variable:
```
set SECRET_KEY=YOUR_SECRET_KEY_FROM_SETTINGS.PY
set DEBUG=True
```

#### Static files:
```
python manage.py collectstatic
```

#### Mirgate:
```
python manage.py makemigrations
or
python manage.py makemigrations blog

python manage.py migrate
```

#### Create Super User:
```
python manage.py createsuperuser
```

#### Start blogging:
```
python manage.py runserver
```
Now go to login page enter ther super user credentials.

#### Tests:
```
pytest
```
