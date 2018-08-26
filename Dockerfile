FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements/ /code/
RUN pip install -r dev.txt
ADD . /code/
