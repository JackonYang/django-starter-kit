# django APP
# do not operate database in APP's docker
# for there would be several apps, sharing one database
#
FROM daocloud.io/python:2.7
MAINTAINER JackonYang <i@jackon.me>>


# http://stackoverflow.com/questions/23524976/capturing-output-of-python-script-run-inside-a-docker-container
ENV PYTHONUNBUFFERED=0


# https://docs.docker.com/engine/reference/builder/#arg
ARG pip_host=pypi.douban.com
ARG pip_root_url=http://pypi.douban.com/simple/

# upgrade pip to latest version
RUN pip install --upgrade pip -i $pip_root_url --trusted-host $pip_host

# python packages
RUN pip install -i $pip_root_url --trusted-host $pip_host django==1.10.3
RUN pip install -i $pip_root_url --trusted-host $pip_host django-grappelli==2.8.1
RUN pip install -i $pip_root_url --trusted-host $pip_host djangorestframework==3.4.7
RUN pip install -i $pip_root_url --trusted-host $pip_host markdown==2.6.7
RUN pip install -i $pip_root_url --trusted-host $pip_host django-filter==0.15.2
RUN pip install -i $pip_root_url --trusted-host $pip_host django-redis==4.4.4
RUN pip install -i $pip_root_url --trusted-host $pip_host rollbar==0.13.8


COPY . /backend
WORKDIR /backend

RUN pip install -r requirements.txt
