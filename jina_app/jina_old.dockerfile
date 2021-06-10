FROM jinaai/jina:master-py38-devel

WORKDIR /app

COPY . app.py /app/

RUN pip install --pre jina
RUN pip install "jina[multimodal]"
RUN pip install -r requirements.txt

EXPOSE 6000

ENTRYPOINT [ "python" ]

CMD [ "/app/app.py" ]