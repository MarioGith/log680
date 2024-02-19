#!/bin/bash

# Script pour configurer et exécuter l'application

export HOST="votre_hote"
export TOKEN="votre_token"
export T_MAX="votre_temp_max"
export T_MIN="votre_temp_min"
export DATABASE="votre_base_de_donnees"

python src/main.py
