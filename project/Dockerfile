FROM python:3.8

LABEL maintainer="Ducnm"

COPY . /app

WORKDIR /app

RUN pip install flask werkzeug

# command to run on container start

CMD [ "python", "DemoCICDK8s.py" ]
