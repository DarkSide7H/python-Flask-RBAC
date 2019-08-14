FROM python:3.6

COPY logging.conf runserver.py requirements.txt /api/
COPY app /api/app
COPY config /api/config
COPY utils /api/utils

WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python" ]

CMD ["runserver.py"]