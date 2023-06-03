# Justification des métriques de type Pull Requests (PR)

## Lead Time de tous les PRs
La première métrique pour les pull requests est le "lead time" d'un pull 
request. Cette métrique est le temps entre le moment où le pull request a été 
créé et le moment où il a été fermé. La moyenne de tous les PRs est aussi 
calculée.

La métrique permet de mieux comprendre la dynamique dans le groupe de 
travail. En effet, un "lead time" trop grand peut signifier qu'il y a un 
goulot d'étranglement lors de la revue de code. Ceci pourrait se produire 
pour diverses raisons : les développeurs tardent à faire les revues, le pull 
request est trop gros et faire la revue prend plus de temps, et ainsi de 
suite. Peu importe la raison, cette métrique permet d'identifier qu'il y a 
une situation qui devrait être investiguer dans le groupe de travail.


## Nombre de PR fusionnés dans une période donnée
Cette métrique calcule le nombre de pull requests qui ont été fusionnés dans 
une période donnée. Il faut simplement calculer le nombre d'instance où un
pull request est "merged" dans la branche "develop" du projet.

Le but de cette métrique est de mieux comprendre la vitesse du flux de travail 
d'une équipe. En effet, la période donnée peut être, par exemple, la durée 
d'un sprint. Ensuite, nous pouvons comparer le nombre de tâches qui ont été 
complétés dans chaque sprint. Ceci permet de faire de meilleurs prédictions 
quant à la quantité de travail qu'une équipe est capable de faire.


## Nombre de lignes de code par PR
Cette métrique calcule le nombre de lignes de code qu'un pull request 
possède.

Pour rendre le flux le plus rapide possible, il est préférable de faire des 
petits pull requests. Un nombre de lignes de code trop élevé est plus 
difficile à corriger pour les réviseurs et peut augmenter considérablement 
le "lead time" du pull request.


## Temps avant le premier commentaire
Cette métrique calcule le temps entre le moment où le pull request est créé 
et le moment du premier commentaire. Une moyenne de tous les pull requests 
est calculée aussi.

La métrique permet de déterminer si les réviseurs sont pro-actifs dans le 
processus de revues de code. Si le temps est trop élevé, cela signifie que 
les réviseurs ne sont pas sufisamment engagés dans le processus de revues de 
code. 

## Nombre de commentaires par PR
Cette métrique calcule le nombre de commentaires dans un PR. Il est aussi 
possible de savoir la moyenne de commentaires dans tous les pull requests.

Une moyenne trop basse signifie qu'il n'y a pas suffisament d'interactions 
entre les réviseurs et le développeur. Un chiffre trop élevé signifie qu'il 
y a un problème. Ce problème peut être pour diverses raisons, dont la 
grosseur du pull request, des divergences d'opinion sur des façons de 
concevoir ou programmer, ou même des spécifications erronées ou imprécises. 
En bref, un nombre moyen de commentaires trop élevé signifie qu'il y a un 
problème à investiguer dans le processus.