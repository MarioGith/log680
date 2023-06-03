# Justification des métriques Kanban

## Lead time pour une tâche donnée
La première métrique pour les métriques Kanban est le calcul du lead time pour
une tâche donnée. Le lead time se calcule en prenant le moment où la tâche a 
été fermée sur GitHub et en le soustrayant de la valeur du moment où la tâche
a été ouverte.

Cette métrique permet de savoir exactement le lead time d'une tâche. Une valeur
élevée peut signifier que la tâche était trop complexe pour une seule carte. 
Advenant que l'équipe n'utilise pas des limites sur le nombre de tâches en cours,
il est aussi possible qu'un développeur fasse trop de tâches simultanément.
Dernièrement, un lead time élevé peut signifier qu'il y a de trop longs temps 
d'attente dans les colonnes. Il faut vérifier avec d'autres métriques pour 
savoir exactement la cause d'un long lead time.

Idéalement, le lead time doit être le plus court possible.

## Lead time pour les tâches terminées dans une période donnée
La deuxième métrique est très similaire à la première : c'est le lead time
pour les tâches terminées dans une période donnée. Pour le calculer, il faut 
calculer tous les lead times des tâches qui sont complétées dans la période 
donnée. Une moyenne est aussi calculée.

Cette métrique est très utile pour les sprints. En effet, la période donnée peut
représenter la date de début et de la fin du sprint. Il est donc possible de 
savoir quelles tâches ont été complétées pendant le sprint.

Idéalement, la valeur de la moyenne des temps doit être basse.

## Nombre de tâches actives pour une colonne donnée
Cette métrique affiche le nombre de tâches actives par colonnes. Le calcul est 
simple : il faut détecter le nombre de tâches dans une colonne et les additionner.

Cette métrique est nécessaire pour détecter, entre autres, les entonnoirs.
S'il y a trop de cartes dans une colonne autre que le "backlog" ou "terminée",
il y a fort probablement un problème à résoudre.

## Nombre de tâches complétés pour une période donnée
Cette métrique additionne le nombre de tâches complétés dans une période donnée.

Elle est très utile pour déterminer le rythme que l'équipe a pour compléter les
tâches assignées. Idéalement, il faut que cette valeur soit élevé. Une valeur
basse devrait être investiguer. En effet, il se pourrait que les tâches sont 
trop grosses. Dans ce cas-là, de nouvelles cartes devraient être créées pour 
réduire la grosseur des cartes.