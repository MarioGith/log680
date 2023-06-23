# Pre-commit git hook
Afin d'assurer la qualité de code à travers l'équipe,
nous avons configuré un pre-commit hook pour automatiser la vérification de la qualité du code avant
chaque commit.
Nous avons défini des étapes de linting, analyse statique de code et de formatage.
Un pre-commit git hook est un script qui est exécuté automatiquement avant un commit.
Des tests unitaires sont exécutés lors de l'exécution du script.
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
          args: [--disable=missing-docstring]

    - repo: local
      hooks:
        - id: unittest
          name: Unit test
          entry: python -m discover unit_testing
          language: python
          pass_filenames: false
    ```
  - Pour installer les scripts qui sont dans la config, utiliser la commande ```pre-commit install```
  - Le pre-commit devrait s'exécuter lorsqu'on fait un git commit
  -
