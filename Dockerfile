# pull the official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app

RUN chmod +x ./entrypoint.sh

# copy project
COPY . /usr/src/app


EXPOSE 8000

ENTRYPOINT [".entrypoint.sh"]

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "collectstatic", "--noinput"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]