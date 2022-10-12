FROM python:3.9

#RUN python3 -m pip install pyomo
#RUN python3 -m pip install gurobipy

#RUN python3 -m pip install xpress --user


#RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install hana_ml

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

#RUN pip3 install flask

COPY ./ app

# Required to execute script for AI Core
RUN chgrp -R nogroup /app && \
    chmod -R 770 /app
