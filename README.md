# Développez une architecture back-end sécurisée en utilisant Django ORM

## Comment executer ce script ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P12_ANTOINE_CARDON.git`
* Allez à la racine du projet via `cd P12_ANTOINE_CARDON`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv env`
* Activez l'environnement virtuel via `source env/bin/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`

* Veuillez installer PostGreSQL avant de continuer l'initialisation du projet.
* Executez cette commande dans votre terminal : `psql -U <votre nom d'utilisateur>`
* Entrez le mot de passe de l'utilisateur renseigné.
* Executez ensuite cette commande : `CREATE DATABASE EPIC_EVENTS ;`
* Vous pouvez ensuite fermer le shell psql via `\q`
* Executez ensuite cette commande pour configurer la base de données dans le projet : `python configure_env.py`
* Suivez les instructions et entrez votre nom d'utilisateur et le mot de passe utilisé pour accéder à la base de données.
* Vous pouvez lancer le projet via la commande `python manage.py runserver`
* ENJOY ! Vous êtes prêt à utiliser l'application !

## Guide d'utilisation de l'application :
Retrouvez tous les endpoints sur https://documenter.getpostman.com/view/20095524/2s93Y3u1Jx

|   Endpoint   |  Méthode |   Description |
|---           |---          |---            |
|http://127.0.0.1:8000/token| POST | Permet d'obtenir un token pour accéder à l'application            |
|http://127.0.0.1:8000/customers/| POST | Permet de créer un client            |
|http://127.0.0.1:8000/customers/| GET | Permet d'obtenir la liste des clients            |
|http://127.0.0.1:8000/customers/:customer_id/| GET | Permet d'obtenir un client via son ID            |
|http://127.0.0.1:8000/customers/:customer_id/| PUT | Permet de modifier un client via son ID            |
|http://127.0.0.1:8000/customers/:customer_id/| DELETE | Permet de supprimer un client via son ID            |
|http://127.0.0.1:8000/events/| GET | Permet d'obtenir la liste des évènements          |
|http://127.0.0.1:8000/events/:event_id/| PUT | Permet de modifier un évènement via son ID |
|http://127.0.0.1:8000/contracts/| POST | Permet de créer un contrat |
|http://127.0.0.1:8000/contracts/:contract_id/| PUT | Permet de modifier un contrat via son ID |
|http://127.0.0.1:8000/contracts/:contract_id/| GET | Permet de lire un contrat via son ID |
