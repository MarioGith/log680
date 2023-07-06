# Variables d'environnement
Afin de faciliter la configuration, nous rendons ces variables qui peuvent être paramétrées:
- l’hôte (HOST),
- le jeton (TOKEN),
- la température maximale (T_MAX),
- la température minimal (T_MIN)
- tickets (TICKETS).

Pour ce faire, nous utilisons la librairie python-dotenv qui nous permet de définir facilement les valeurs de ces variables dans un fichier .env, qui ne doit pas être publié dans notre repository git.

1. Installer python-dotenv: ```pip install python-dotenv```
2. Créer un fichier .env dans la racine du projet

Contenu du fichier .env:
```
HOST = ""
OXYGENCS_TOKEN = ""
T_MAX = ""
T_MIN = ""
TICKETS = ""
```
3. Dans les fichiers qui utilisent des variables d'environnement, ajouter:
```
from dotenv import load_dotenv
load_dotenv()
```
