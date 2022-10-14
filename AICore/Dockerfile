FROM python:3.9

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./ app

# Required to execute script for AI Core
RUN chgrp -R nogroup /app && \
    chmod -R 770 /app
