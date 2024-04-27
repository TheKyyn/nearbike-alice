# Serveur Alice

## Description

Serveur Alice est une application web Flask qui gère l'interface utilisateur pour une application de facilitation de parcours à vélo pour les usagers de la ville de Paris. Ce serveur permet l'authentification des utilisateurs, la gestion des stations Vélib favorites, et affiche les données récupérées du Serveur Bob.

## Fonctionnalités
- Authentification des utilisateurs (inscription, connexion, déconnexion)
- Gestion des stations Vélib favorites (ajout, suppression, affichage)
- Affichage des informations des stations Vélib

## Technologies Utilisées
- Flask
- Flask-Login pour la gestion des sessions
- Flask-Bcrypt pour le hashing des mots de passe
- Flask-SQLAlchemy pour l'interaction avec la base de données
- MariaDB comme système de base de données

## Installation

### Prérequis
- Python 3
- pip
- MariaDB

### Configuration de l'environnement
```bash
# Création d'un environnement virtuel
python -m venv venv
```

# Activation de l'environnement virtuel
```bash
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate  # Sur Windows
```

# Installation des dépendances
```bash
pip install -r requirements.txt
```

### Configuration de la base de données
Assurez-vous que MariaDB est installé et configuré correctement, puis créez une base de données pour l'application.

### Lancement de l'application
```bash
# Initialisation de la base de données
flask db upgrade

# Lancement du serveur
flask run
```

### Usage

Accédez à l'application via http://localhost:5000 après le lancement du serveur. Utilisez les routes définies pour l'inscription, la connexion, et la gestion des favoris.

### Contribution

Les contributions à ce projet sont bienvenues. Veuillez suivre les pratiques standard pour proposer des améliorations ou des corrections.

### Licence

Ce projet est sous licence libre, vous pouvez le redistribuer et/ou le modifier selon les termes de la Licence Publique Générale GNU publiée par la Free Software Foundation.
