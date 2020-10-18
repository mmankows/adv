# Adverity task

## Setup & Usage
In order to run this app you'd need `docker` installed.

- Run `cd /tmp/ && git clone git@github.com:mmankows/adv.git && cd adv && docker-compose up`
- Open http://localhost:8080

## TODOs
There's bunch of TODOs in different places in the code for things that could/should be improved.

Additional points left:
- Currently statics are served by webpack dev server - 
prepare prod build and serving static frontend files, 
either from dedicated server or using Django addon `whitenoise`.
- Deploy it live

## Additional comments
SWAPI is no longer deployed nor maintained and required additonal effort to dockerize it.
