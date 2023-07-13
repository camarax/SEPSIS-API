# Projet API Backend de Prédiction du Sepsis

Ce projet implémente une API backend pour effectuer des prédictions du sepsis à partir des caractéristiques d'un individu. L'API est basée sur le framework Flask et utilise un modèle pré-entraîné pour effectuer les prédictions.

## Installation

Pour exécuter l'API, vous devez suivre les étapes suivantes :

1. Clonez ce dépôt de code sur votre machine locale.

2. Assurez-vous d'avoir Python 3.7 ou une version ultérieure installée.

3. Installez les dépendances requises en exécutant la commande suivante :

   ```bash
   pip install -r requirements.txt

4. Lancez l'API en exécutant le fichier **'index.py'** :

   ```bash
   python index.py

5. L'API sera accessible à l'adresse **'http://localhost:5000'**.

## Fonctionnalités de l'API

L'API fournit les fonctionnalités suivantes :

- Endpoint /predict : Ce point de terminaison permet de faire des prédictions de sepsis. Il attend une requête POST contenant les caractéristiques d'un individu au format JSON. Les caractéristiques attendues sont les suivantes : "PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age", "Insurance". L'API renvoie la prédiction de sepsis et la probabilité associée.
- Endpoint /health : Ce point de terminaison permet de vérifier l'état de l'API. Il renvoie simplement un message "Okay" pour indiquer que l'API est opérationnelle.

## Authentification

L'API utilise une authentification basée sur les jetons d'accès. Pour accéder aux endpoints de l'API, vous devez inclure le jeton d'accès dans l'en-tête "Authorization" de chaque requête. Par défaut, le jeton d'accès valide est défini comme "lesecret". Vous pouvez personnaliser la logique de validation du jeton d'accès en implémentant la fonction validate_token dans le fichier index.py.

## Tests

Le fichier **'testSepsis.py'** contient des tests unitaires pour vérifier le bon fonctionnement des différentes fonctions de la classe **'Sepsis'**. Vous pouvez exécuter ces tests en exécutant le fichier avec la commande suivante :

   ```bash
   python -m unittest discover
````

Assurez-vous d'avoir les dépendances nécessaires installées avant d'exécuter les tests.

## Documentation

La documentation complète du code backend de l'API est disponible dans le fichier documentation_backend.md. Il fournit des informations détaillées sur les différentes classes, fonctions et points de terminaison de l'API.

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous souhaitez apporter des améliorations, veuillez soumettre une demande d'extraction avec vos modifications.

## Auteurs

Ce projet a été développé par **Aboubacar CAMARA**, **Aaricia DOMINGUEZ** et **Adrien ALVAREZ** dans le cadre du projet annuel de l'école ESGI Lyon. Si vous avez des questions, veuillez nous contacter à l'adresse **aa-dz@hotmail.com** ou **aboubacar.camara.abk@gmail.com**.
