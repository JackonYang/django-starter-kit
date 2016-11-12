PY?=python
PIP?=pip

server:
	$(PY) manage.py runserver 0.0.0.0:8000


############# data and migratations

makemigrations:
	$(PY) manage.py makemigrations

migrate:
	$(PY) manage.py migrate

superuser:
	$(PY) manage.py createsuperuser


############# env setup

build:
	$(PIP) install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r requirements.txt


.PHONY: build
.PHONY: server makemigrations migrate superuser
