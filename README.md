# Projet 10 -  SoftDesk

![made_with_python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![made_with_django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![made_with_sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


## Description

SoftDesk est une API.

Les points de terminaisons de cette API servent à une application permettant le suivi de projets, de façon générale :

- affecter des contributeurs aux différents projets
- remonter les problèmes rencontrés sur les projets
- écrire des commentaires en lien avec ces problèmes

L'utilisation de cette API nécessite une authentification.

## Installation

Cette API exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de pipenv est recommandé, mais des instuctions utilisant venv et pip sont également fournies plus bas.

### Installation et exécution de l'application avec pipenv

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/Aponovi/SoftDesk.git` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/Aponovi/SoftDesk/archive/refs/heads/main.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `$ cd SoftDesk`
3. Installez les dépendances du projet à l'aide de la commande `pipenv install`
4. Démarrer le serveur avec `pipenv run python manage.py runserver`

Les étapes 1 à 3 ne sont requises que pout l'installation initiale.Pour les lancements ultérieurs du serveur, il suffit d'exécuter l'étape 4 à partir du répertoire racine du projet.
### Installation et exécution de l'application sans pipenv (avec venv et pip)

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone (https://github.com/Aponovi/SoftDesk.git)` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/Aponovi/SoftDesk/archive/refs/heads/main.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `$ cd SoftDesk`
3. Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Démarrer le serveur avec `$ python manage.py runserver`

Les étapes 1 à 5 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur, il suffit d'exécuter les étapes 4 et 6 à partir du répertoire racine du projet.


## Utilisation

Une fois que vous avez lancé le serveur, rendez-vous sur un navigateur web à l'adresse http://localhost:8000/


### Documentation

Disponible sur postman : https://documenter.getpostman.com/view/20943323/UyxqB3C1
