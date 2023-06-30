# Utilisez l'image de base Python appropriée
FROM python:3.11

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel votre application écoute
EXPOSE <PORT>

# Démarrez l'application
CMD ["python", "main.py"]
