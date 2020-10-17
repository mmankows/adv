FROM python:3.6
# TODO: try upgrading to python 3.7
# "petl has been tested with Python versions 2.7 and 3.4-3.6 under Linux and Windows operating systems"

RUN apt-get update && apt-get install -y \
       bash \
       gcc \
       make \
       postgresql \
       python3-dev

# Instal requirements and add code - use docker cache
COPY /requirements.txt /code/requirements.txt

# TODO: use poetry
RUN pip install -r /code/requirements.txt

COPY . code
WORKDIR code

EXPOSE 8000

# TODO: run through uwsgi server, get rid of manage.py
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]