FROM python:3.8.8-slim-buster

WORKDIR /app

COPY ./* /app/

RUN apt-get update && apt-get install curl -y

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

#ENTRYPOINT [ "python" ]
#
#CMD [ "app.py" ]