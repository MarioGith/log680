FROM python:3.9-slim-bullseye

# Environment variables
ENV APP_PATH="/usr/src/app" \
    APP_USER="oxygenadmin" \
    PYTHONUNBUFFERED=1
 
 # Define work directory
WORKDIR ${APP_PATH}

# User setup + apt update
RUN adduser --system --no-create-home $APP_USER
RUN apt update
RUN apt-get --assume-yes install gcc libpq-dev

COPY Pipfile ${APP_PATH}
COPY Pipfile.lock ${APP_PATH}
RUN pipenv install

COPY . ${APP_PATH}

CMD pipenv run start