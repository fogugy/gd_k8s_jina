FROM python:3.8.8-slim-buster

WORKDIR /app

COPY ./* /app/

RUN apt-get update && apt-get install curl -y

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

ENV JINA_PORT 6000
ENV HW_WORKDIR workdir

EXPOSE 6000

#ENTRYPOINT [ "python" ]
#
#CMD [ "/app/app.py", "-" ]