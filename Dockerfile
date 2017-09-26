FROM python:alpine

MAINTAINER Larry Hignight

RUN pip install pip
RUN pip install flask
RUN pip install flask-login
RUN pip install flask-openid
RUN pip install flask-mail
RUN pip install flask-sqlalchemy
RUN pip install sqlalchemy-migrate
RUN pip install flask-whooshalchemy
RUN pip install flask-wtf
RUN pip install flask-babel
RUN pip install guess_language
RUN pip install flipflop
RUN pip install coverage

RUN mkdir -p /src
COPY run.py /src
COPY config.py /src
COPY app /src/app
WORKDIR /src
CMD ["python", "run.py"]
