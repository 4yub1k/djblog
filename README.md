# My Blog

My blog is simple neat and clean blog site built with Django, HTMX, and Bootstrap 5.

![](https://img.shields.io/badge/Django-4.1.6-green)
![](https://github.com/4yub1k/djblog/actions/workflows/myBlog.yml/badge.svg)
![](https://img.shields.io/badge/Release-0.0.2-orange)

### Release 0.0.2:
  [Summernote WYSIWYG Editor Added](#edit-post)
  
![image](https://user-images.githubusercontent.com/45902447/218198174-d13d5e76-1dd4-448d-b868-88779e9cae82.png)

<hr>

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
Now go to login page enter super user credentials.

#### Tests:
```
pytest
```
#### Home Page:
![image](https://user-images.githubusercontent.com/45902447/218100011-89e5be96-af6c-45c1-8ec9-f9bf30f96bc8.png)

#### Login Page:
![image](https://user-images.githubusercontent.com/45902447/218100144-c4f2c029-4574-41f4-98ea-049d411ec16b.png)

#### Registration Page:
![image](https://user-images.githubusercontent.com/45902447/218100250-40e72d8a-c679-480c-b34f-4f353e5b29d3.png)

#### Edit Post:
![image](https://user-images.githubusercontent.com/45902447/218264080-9e966f87-d18a-4852-bfa3-967a3c7bec32.png)

#### Post:
![image](https://user-images.githubusercontent.com/45902447/218100563-d6e0e92d-a264-4ca8-bbca-4281247c6fac.png)


