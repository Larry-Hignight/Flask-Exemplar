FROM python:alpine

MAINTAINER Larry Hignight

RUN pip install flask

COPY app /src/app
copy run.py /src
EXPOSE 5000
ENTRYPOINT ["python", "/src/run.py"]


