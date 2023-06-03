# Colonnes Kanban et Workflows

## Colonnes Kanban
Le projet utilise 5 colonnes Kanban : backlog, à faire, en cours, revue, et 
terminée. L'équipe a gardé seulement cinq colonnes pour garder le Kanban simple
à utiliser ; trop de colonnes rend l'utilisation encombrante et difficile à 
visualiser.

### Backlog
Toutes les tâches créées sont mises dans le backlog. Les tâches ici ne sont pas
encore sélectionnés à faire prochainement dans la semaine suivante.

### À faire
Les tâches dans la colonne "à faire" sont des tâches qui ont été sélectionnés 
pour être complétés durant la prochaine semaine.

### En cours
Les tâches dans la colonne "en cours" sont présentement sélectionnés par une 
personne. Ces tâches sont en train d'être implémentées.

### Revue
Les tâches dans la colonne "revue" sont en cours de révision. Elles sont 
d'habituellement dans un "pull-request" en attendre de rétroaction de la part
d'autres développeurs du projet.

### Terminée
Les tâches dans la colonne "terminée" sont considérés comme étant complétés. 
Un développeur l'a fermée.

## Workflows
Pour simplifier la tâche des développeurs, les "workflows" ci-dessous ont été
ajoutés au projet pour l'automatisation.

### Item added to project
Lorsqu'une tâche est créée, elle est automatiquement transférée dans la 
colonne "backlog" du tableau Kanban.

### Item reopened
Advenant qu'il soit nécessaire de rouvrir une tâche fermée, elle est 
transférée dans la colonne "en cours".

### Item closed
Lorsqu'une tâche est fermée (d'habituellement dans la colonne revue), elle est 
transférée automatiquement dans la colonne "terminée". Il peut arriver toutefois 
qu'une tâche soit fermée plus tôt dans le processus, par exemple s'il y a une 
tâche qui est le double d'une autre ou qui n'est plus dans les plans.

### Code changes requested
Lorsqu'un pull request reçois une demande de changement du code, le pull 
request retourne dans la colonne "à faire". C'est au développeur de la 
transférer dans la colonne "en cours" lorsqu'il sera le temps de la retravailler.

### Code review approved
Lorsqu'un pull request est approuvée, le pull request est transférée dans la 
colonne "revue".

### Pull request merged
Lorsqu'un pull request est fusionné, le pull request est transféré dans la 
colonne "terminée".
