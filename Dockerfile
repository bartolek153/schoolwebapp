############################################################
# Dockerfile to build Flask App
# Based on https://github.com/carlostighe/apache-flask
############################################################

# docker build -t schoolwebapp .
# docker run --rm -d -p 80:80 --name <name> -v $(pwd):/var/www/apache-flask/ schoolwebapp 

# Set the base image
FROM debian:bullseye-slim

# File Author / Maintainer
LABEL image.author="carlos.tighe@universityofgalway.ie"

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY requirements.txt /var/www/apache-flask/app/requirements.txt
RUN pip install -r /var/www/apache-flask/app/requirements.txt

# Copy over the apache configuration file and enable the site
COPY apache-flask.conf /etc/apache2/sites-available/apache-flask.conf

# Copy over the wsgi file, run.py and the app
COPY . /var/www/apache-flask/

RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf
RUN a2enmod headers

# LINK apache config to docker logs.
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

RUN chmod a+w /var/www/apache-flask/src/database/db.json

EXPOSE 80

WORKDIR /var/www/apache-flask
# VOLUME /var/www/apache-flask

CMD  /usr/sbin/apache2ctl -D FOREGROUND