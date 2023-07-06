# Explication du processus d'intégration continue du projet

Le projet a deux pipelines : un pour Metrics et un autre pour Oxygen-CS. Ces
pipelines sont utilisés pour l'intégration continue de ces deux projets.

Lorsqu'un utilisateur pousse du code sur la branche "main" d'un projet
(principalement) par le biais d'un "pull request", un déclencheur est activé
qui démarre le pipeline du projet (fichier
[.github/workflows.main.yaml](https://github.com/CAMaji/oxygen-cs-grp2-eq10/blob/main/.github/workflows/main.yml)
pour le projet Oxygen-CS).

Le pipeline utilise quelques secrets qui sont stockés dans une voûte sur
GitHub. Par exemple, le nom d'utilisateur et le mot de passe du compte
DockerHub sont stockées dans les variables DOCKERHUB_USERNAME et
DOCKERHUB_PASSWORD respectivement.

La section "env" du pipeline décrit toutes les variables utilisées par au moins
l'une des tâches du pipeline. Certains utilisent des secrets, d'autres non.

## Jobs
Les tâches (jobs) du pipeline sont séparées en deux grandes catégories : le
"setup" et l'assurance-qualité (QA), et la partie DockerHub.

### Setup et QA
Cette catégorie possède 5 sous-tâches. Premièrement, le pipeline extrait le
code source à l'aide d'un "checkout". Deuxièmement, le pipeline installe la
version 3.11 de Python. Troisièmement, les dépendances nécessaires pour
l'exécution des tâches dans cette catégorie sont téléchargées et installées,
dont le fichier libraries.txt. Quatrièmement, les tests unitaires sont exécutées
(trois commandes python pour le projet Metrics (pour les tests des métriques
de type pull requests, kanban, ou pipeline) et une seule pour le projet
Oxygen-CS pour les variables de configuration). Finalement, des hooks pour le
linting, le formatage, et l'analyse de code statique sont exécutées.

Advenant que les tests unitaires échouent ou que le code ne passe pas à travers
les standards d'assurance-qualité des hooks, le pipeline échoue. La prochaine
catégorie ne sera donc pas exécutée.

### DockerHub
Cette catégorie possède 4 sous-tâches. D'abord, un nouveau "checkout" est
exécuté pour acquérir le code source nécessaire pour les étapes suivantes.
Ensuite, le pipeline se connecte sur le compte DockerHub de l'équipe. Par
après, le pipeline extrait des méta-données (utilisé pour le tag "latest").
Finalement, le pipeline crée une image Docker, puis la publie sur DockerHub.

Une fois que l'image est créée sur DockerHub, l'utilisateur peut aller
télécharger la version la plus récente (latest), ou télécharger une image
précédente. Les images sont nommées avec les tags suivants : metrics-1.XX et
oxygencs-1.XX, où les XX représentent la version du pipeline exécuté.

L'utilisateur peut ensuite exécuter l'image sur son Docker pour démarrer
l'application. L'utilisateur doit cependant fournir à l'image les paramètres
de configuraiton nécessaire pour l'exécution du code. Le projet Metrics
nécessite un TOKEN pour accéder aux projets GitHub, tandis que le projet
Oxygen-CS nécessite les paramètres HOST (adresse IP pour accéder au système
central de chauffage), un OXYGENCS_TOKEN (code fournie par le chargé de
laboratoire), un TICKETS (nombre de ticks pour augmenter ou descendre la
température, un T_MIN (température minimale, et un T_MAX (température maximale).
