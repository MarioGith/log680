FROM python:3.8-alpine

WORKDIR /src

COPY . /src

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --deploy

EXPOSE 80

CMD ["pipenv", "run", "start"]

