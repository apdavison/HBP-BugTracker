#
# Build an image for deploying the Neuromorphic Platform job manager
#
# To build the image, from the parent directory:
#   docker build -t nmpi_queue_server -f job_manager/Dockerfile .
#
# To run the application:
#  docker run -d -p 443 nmpi_queue_server
#
# To find out which port to access on the host machine, run "docker ps"
#
# To check the content of the docker container:
#   sudo docker run -it nmpi_server /bin/bash

FROM debian:jessie
# MAINTAINER Andrew Davison <andrew.davison@unic.cnrs-gif.fr>


ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --fix-missing; apt-get -y -q install nano python-dev python-setuptools sqlite3 postgresql python-psycopg2 git supervisor build-essential python-numpy nginx-extras
RUN easy_install pip
RUN pip install --upgrade pip
RUN unset DEBIAN_FRONTEND

RUN pip install uwsgi

ENV SITEDIR /home/docker/site

COPY . $SITEDIR
COPY packages /home/docker/packages
COPY issuetracker/static /home/docker/static

# COPY simqueue /home/docker/simqueue
# COPY quotas /home/docker/quotas
# COPY build_info.json $SITEDIR

WORKDIR /home/docker

RUN pip install -r $SITEDIR/requirements.txt

RUN pip install $SITEDIR/packages/task-types-0.0.10
RUN pip install $SITEDIR/packages/bbp-services-0.0.15
RUN pip install $SITEDIR/packages/hbp-app-python-auth-0.1.5
RUN pip install $SITEDIR/packages/bbp-client-0.4.4

ENV PYTHONPATH  /home/docker:/home/docker/site:/usr/local/lib/python2.7/dist-packages:/usr/lib/python2.7/dist-packages

WORKDIR $SITEDIR
RUN if [ -f $SITEDIR/db.sqlite3 ]; then rm $SITEDIR/db.sqlite3; fi
RUN python manage.py check


RUN mkdir -p /home/docker/components 
RUN python manage.py collectstatic --noinput
RUN unset PYTHONPATH

# nginx config
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s $SITEDIR/deployment/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s $SITEDIR/deployment/supervisor-app.conf /etc/supervisor/conf.d/
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log


# COPY . /home/docker/code/


EXPOSE 443
CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisor-app.conf"]


