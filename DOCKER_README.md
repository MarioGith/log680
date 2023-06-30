## Prérequis 

1. Docker : https://docs.docker.com/get-docker/
1. Docker Compose : https://docs.docker.com/compose/install/

## Configuration
```docker-compose.yml```

Ce fichier définit la configuration pour le service de l'application.

### service oxygen-cs :
- build: Spécifie le contexte de construction à utiliser (répertoire courant).
- ports: Associe le port 80 du conteneur au port 4000 de la machine hôte.
- environment: Définit les variables d'environnement pour la configuration de l'application.

## Dockerfile
Ce fichier définit comment Docker doit construire une image personnalisée pour l'application.

- FROM python:3.8-alpine: Spécifie l'image de base.
- WORKDIR /src: Définit le répertoire de travail à l'intérieur du conteneur.
- COPY . /src: Copie les fichiers de l'application dans le conteneur.
- RUN python -m pip install --upgrade pip: Met à jour pip.
- RUN pip install pipenv && pipenv install --dev --deploy: Installe les dépendances de l'application.
- EXPOSE 80: Expose le port 80.
- CMD ["pipenv", "run", "start"]: Définit la commande par défaut pour démarrer l'application.

## Construction et Exécution

```docker-compose up --build```

vous pouvez y accéder en allant sur http://localhost:4000 dans votre navigateur.