# syntax=docker/dockerfile:1
FROM python:latest

# install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install requests==2.30.0
RUN pip install Flask==2.3.2
RUN pip install Flask-RESTful==0.3.10
RUN pip install flask-swagger-ui==4.11.1
RUN pip install swagger-ui-bundle==0.0.9
RUN pip install flasgger==0.9.7.1
RUN pip install pytest==7.3.1
RUN pip install coverage==7.2.6
RUN pip install psycopg2-binary==2.9.6
RUN pip install signalrcore
RUN pip install python-dotenv

# copy all files of metrics project into the docker file
COPY src/main.py /

# run the file
CMD [ "python", "-u", "/main.py"]