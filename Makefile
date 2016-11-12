PY?=python
PIP?=pip
DJANGO_STARTER_KIT_REPO?=https://github.com/JackonYang/django-starter-kit.git

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


############# sync

sync-init:
	git checkout -b sync sync-latest

sync-update:
	git pull $(DJANGO_STARTER_KIT_REPO) sync:sync

sync-done:
	git tag -f sync-latest
	git push $(DJANGO_STARTER_KIT_REPO) sync:sync
	git checkout master
	git merge sync
	git branch -d sync



.PHONY: build
.PHONY: server makemigrations migrate superuser
