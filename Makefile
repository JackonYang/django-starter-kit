PY?=python
PIP?=pip
DJANGO_STARTER_KIT_REPO?=https://github.com/JackonYang/django-starter-kit.git
FIRST_COMMIT?=899b9c5c7bb3a310dbb899d98a72ca219ce6cc27

server:
	$(PY) manage.py runserver 0.0.0.0:8000


debug:
	docker-compose run --service-ports web /bin/bash


############# unit test

test:
	pytest --cov ./ --cov-report term-missing:skip-covered --capture=no


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


############# env setup

crawler:
	$(PY) manage.py runscript crawler


############# sync

sync-start:
	git checkout -b sync $(FIRST_COMMIT)
	git pull $(DJANGO_STARTER_KIT_REPO) sync:sync

sync-done:
	git push $(DJANGO_STARTER_KIT_REPO) sync:sync
	git checkout master
	git merge sync
	git branch -d sync


.PHONY: build
.PHONY: server makemigrations migrate superuser
.PHONY: sync-start sync-done
.PHONY: test
.PHONY: debug
