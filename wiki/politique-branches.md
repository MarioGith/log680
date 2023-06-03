# Politique de branches
Le projet utilise la politique de branches Gitflow.

Gitflow a trois niveaux de branches: main, develop, et features.

### Main
Dans le cadre de ce projet, la branche "Main" est seulement utilisé pour les
remises des laboratoires. Donc, la branche reste vide jusqu'à temps qu'une 
remise soit faite. Cette décision a été prise pour rendre clair quelle 
version doit être prise pour l'évaluation du projet.

### Develop
La branche "Develop" est la branche principale des développeurs. Chaque fois
qu'une nouvelle fonctionnalité est créée dans une branche feature, un pull 
request doit être envoyer pour fusionner la branche feature dans la branche 
"Develop". 

Le code doit normalement être approuver par les pairs lors de revues de code 
qui sont attachées aux pull requests. Au besoin, les développeurs peuvent 
écrire des commentaires pour donner de la rétroaction.

### Features
Les branches "Features" sont celles où les tâches sont implémentées. Chaque 
fois qu'un développeur travaille sur une nouvelle tâche, le développeur doit 
créer une nouvelle branche. Le nom de la branche commence par le numéro de 
la tâche sur GitHub et est suivi par un descriptif pertinent.

Exemples : 
- 11-metrique-issue-lead-time-periode
- 22-creer-wiki
- 34-creer-l'infrastructure-pour-l'API

Pour des informations additionnelles sur Gitflow, veuillez consulter [cette ressource](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).