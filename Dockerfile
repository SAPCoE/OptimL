FROM python:3.9

#FROM opensuse/leap:15.2
#RUN zypper --non-interactive update && \
#    zypper --non-interactive install --no-recommends --force-resolution \
#    python3 python3-pip vim tar gzip ncompress 

RUN python3 -m pip install pyomo
RUN python3 -m pip install gurobipy

RUN python3 -m pip install xpress --user


RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install hana_ml

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

#RUN pip3 install flask

COPY ./ app


ENTRYPOINT [ "python" ]
EXPOSE 5000
CMD [ "/app/app.py" ]