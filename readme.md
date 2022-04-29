# Base de publications scientifiques


## Contexte du projet  

> Le centre de recherche Breizhmeiz International souhaite un petit module d'accès simple aux publications scientifiques. On vous demande de mettre en place une base de données MongoDB, orientée documents, pour gérer l'accès à ces publications.   
De votre coté, vous allez tester les datas grâce à un petit script Python.


## choix de l'environnement

Nous souhaitons pour effectuer ces opérations créer un containeur mongodb et un containeur python.  
Le containeur python est créé à partir d'un Dockerfile, sur la base de la dernière image python disponible sur Docker.

Les deux containeurs sont orchestrés par docker compose, des volumes sont créés pour la persistance des données.

Le containeur est créé par la commande : 

> docker-compose up -d --build





## création de la base de données : 

Nous disposons d'un fichier json pour créer la base de données. Ce fichier est copié dans le dossier <i>home</i> du containeur mongodb nommé mongodb3

> docker cp dblp.json mongodb3:/home/dblp.json

puis, dans le containeur, en bash, nous exécutons :

> mongoimport --db DBLP --collection publis --authenticationDatabase admin --username **** --password **** --file /home/dblp.json

Nous disposons de 15000 entrées.

## requêtes : 

pour effectuer les requêtes, nous créons un fichier app.py dans le containeur python, et utilisons la librairie pymongo comme intermédiaire mongo. Afin d'avoir une visualisation dans le terminal des résultats des requêtes (ce qui est demandé), il faut se connecter au <i>bash</i> du containeur : 

> docker exec -it test_python_1 bash

et exécuter le fichier python procédural :

> python app.py


