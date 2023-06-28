# Choix de base de donnée

Nous avons décider d'utiliser une base de donnée relationnelle local puique l'utilisation qu'on doit en faire ne requiert pas d'avoir une base de donnée centralisé. 
Alors nous y sommes aller avec MySQL afin de rester dans la simplicité.

Il n'y a seulement qu'une table qui servira a contenir les différents snapshots faire par l'api.

##### Colonnes

| Colonne | Explication |
| ----------- | ----------- |
|id| identifiant du snapshot|
|timestamp| Date et temps de l'exécution du snapshot|
|backlog| Nombre de tâches dans le backlog|
|a_faire| Nombre de tâches dans la colonne a_faire|
|en_cours| Nombre de tâches dans la colonne en_cours|
|revue| Nombre de tâches en revue|
|termine| Nombre de tâches termine|
