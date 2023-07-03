# Utilisez l'image de base Python appropriée
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

#Installez pipenv
RUN pip install pipenv

# Définir variable env
ENV PYTHONUNBUFFERED=1

#Copiez le fichier pipfile.lock
COPY Pipfile Pipfile.lock ./

#Installez depedences avec pipenv
RUN pipenv install

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Exposez le port sur lequel votre application écoute
EXPOSE 80

# Démarrez l'application
CMD ["pipenv", "run", "start"]
