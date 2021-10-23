# Thinh Blog

[![Django CI](https://github.com/thinhcode/thinhblog-dj/actions/workflows/django.yml/badge.svg?branch=v2)](https://github.com/thinhcode/thinhblog-dj/actions/workflows/django.yml)

Create a blog with Django

## Running
### Windows
```bat
> python .\manage.py runserver
```
The website will run at [localhost:8000](http://localhost:8000).

## Testing
### Windows
```bat
> coverage run manage.py test
> coverage html
```
Opening `/htmlcov/index.html` by Browser to see the test report.

## Dependencies

- [coverage](https://pypi.org/project/coverage/6.0.2/): 6.0.2
- [Django](https://pypi.org/project/Django/3.2.8/): 3.2.8

---
&copy; Thinh Nguyen
