# Justification de la métrique de visualisation
Cette métrique enregistre le nombre de tâches associées à toutes les colonnes 
d'un projet dans une base de données. Pour obtenir le nombre de tâches sur une 
colonne, il faut utiliser le même calcul fait par la métrique Kanban sur le 
nombre de tâches actives sur une colonne donnée. Cependant, il faut le faire sur
toutes les colonnes du projet. 

Cette métrique est très utile. Elle permet de garder un "snapshot" de l'état du
Kanban. Si elle est utilisée régulièrement (par exemple, à chaque jour), il est 
possible de voir l'état du tableau Kanban lors d'une date spécifiée. Il est aussi 
possible de voir l'évolution du Kanban dans un mois. Elle permet d'identifier
les goulots d'étranglement plus facilement.

Elle doit cependant garder le même état pour la structure des colonnes. En effet,
si le nombre de colonnes changent, il devient beaucoup plus difficile de faire des 
comparaisons dans le temps.