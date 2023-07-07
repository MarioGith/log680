# Pre-commit git hook
Afin d'assurer la qualité de code à travers l'équipe,
nous avons configuré un pre-commit hook pour automatiser la vérification de la qualité du code avant
chaque commit.
Nous avons défini des étapes de linting, analyse statique de code et de formatage.
Un pre-commit git hook est un script qui est exécuté automatiquement avant un commit.
Seulement les fichiers qui ont eu de nouvelles modifications sont analysés.
Des tests unitaires sont exécutés lors de l'exécution du script. Si une étape ne passe pas, le commit
est refusé.
## Librairies
- Pylint (linter): ```pip install pylint```
- Black (formateur) ```pip install black```
- pre-commit: ```pip install pre-commit```
  - Créer et Configurer le fichier ```.pre-commit-config.yaml```
    - Exemple:
    ```
    repos:
    - repo: https://github.com/pre-commit/pre-commit-hooks
      rev: v3.2.0
      hooks:
        - id: trailing-whitespace
        - id: end-of-file-fixer
        - id: check-yaml
        - id: check-added-large-files
    - repo: https://github.com/psf/black
      rev: 23.3.0
      hooks:
        - id: black
          language_version: python3.11
          types: [python]
    - repo: https://github.com/PyCQA/pylint
      rev: v2.17.4
      hooks:
        - id: pylint
          args:
            - --disable=C0114,C0115,C0116,R0914,R0801,W0719,E0401
            - --fail-under=4

    - repo: local
      hooks:
        - id: unittest
          name: Unit test
          entry: py -m unittest discover -s unit_testing/app
          language: system
          pass_filenames: false

    ```
  - Pour installer les scripts qui sont dans la config, utiliser la commande ```pre-commit install```
  - Le pre-commit devrait s'exécuter lorsqu'on fait un git commit

### Pylint
Pour l'étape de linting, nous avons défini un seuil de 4.0 pour le score. Nous avons désactivé plusieurs règles que nous considérons pas importantes, par exemples:
- missing-module-docstring (C0114): absence de commentaire pour modules.
- missing-class-docstring (C0115): absence de commentaire pour classes.
- missing-function-docstring (C0116): absence de commentaire pour fonctions.
- too-many-locals (R0914): trop de variables locales dans une fonction ou methode.
- duplicate-code (R0801): duplication de code retrouvé dans plusieurs fichiers.
- boad-exception-raised (W0719): les exceptions soulevées sont trop génériques.
- import-error (E0401): échec d'importation d'un module.

### Analyse statique du code
Pour l'étape d'analyse statique du code, les règles que nous avons choisi sont:
- trailing-whitespace: supprime les whitespaces à la fin d'une ligne de code.
- end-of-file-fixer: assure que les fichiers se terminent par une nouvelle ligne et uniquement une nouvelle ligne.
- check-yaml: vérifie le syntax des fichiers yaml
- check-added-large-files: refuse les fichiers trop larges
-
