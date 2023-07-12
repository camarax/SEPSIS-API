# Documentation du code backend de l'API

Ce document fournit une documentation complète du code backend de l'API. Il décrit les différentes classes, fonctions et points de terminaison utilisés dans le code.

## Fichier index.py

Ce fichier est le point d'entrée de l'API et contient les définitions des points de terminaison ainsi que la logique d'authentification.

### Fonction 'validate_token(token)'

Cette fonction permet de valider un jeton d'accès. Par défaut, elle compare le jeton fourni avec la chaîne "lesecret". Vous pouvez personnaliser cette fonction en implémentant votre propre logique de validation.

### Décorateur 'require_token(func)'

Ce décorateur est utilisé pour vérifier si un jeton d'accès est valide avant d'exécuter une fonction. Il extrait le jeton d'accès de l'en-tête "Authorization" de la requête et appelle la fonction **'validate_token'** pour vérifier sa validité. Si le jeton est invalide ou manquant, une erreur 401 Unauthorized est renvoyée.

### Point de terminaison '/predict'

Ce point de terminaison est accessible via une requête POST à l'URL "/predict". Il attend un objet JSON contenant les caractéristiques d'un individu et renvoie la prédiction de sepsis et la probabilité associée. La fonction predict() de la classe Sepsis est utilisée pour effectuer la prédiction.

## Point de terminaison '/health'

Ce point de terminaison est accessible via une requête GET à l'URL "/health". Il renvoie un message JSON indiquant l'état de santé de l'API. La fonction **'health()'** de la classe **'Sepsis'** est utilisée pour renvoyer la réponse.

## Fichier Sepsis.py

Ce fichier contient la définition de la classe **'Sepsis'**, qui gère les prédictions de sepsis.

### Classe Sepsis

La classe **'Sepsis'** dispose des méthodes suivantes :

**'__init__()'**

Cette méthode initialise l'instance de la classe et définit la variable **'model'** à **'None'**.

**'predict(model_name, data)'**

Cette méthode effectue la prédiction de sepsis en utilisant le modèle spécifié par **'model_name'** et les données fournies dans **'data'**. Elle charge le modèle à partir du fichier spécifié, effectue la prédiction et renvoie les résultats formatés.

**'health()'**

Cette méthode renvoie un message JSON indiquant que l'API est en bon état de fonctionnement.

**'_verify_dictionaris_containt_string(data)'**

Cette méthode vérifie si les données fournies contiennent une chaîne de caractères. Elle itère sur toutes les clés et valeurs de **'data'** et renvoie **'True'** si une valeur est une chaîne de caractères. Sinon, elle renvoie **'False'**.

**'_verify_dictionaris_equals(data)'**

Cette méthode vérifie si les clés de **'data'** correspondent à un ensemble spécifique de clés attendues. Si les clés ne sont pas identiques, elle renvoie **'True'**. Sinon, elle renvoie **'False'**.

## Fichier testSepsis.py

Ce fichier contient les tests unitaires pour vérifier le bon fonctionnement des différentes fonctions de la classe **'Sepsis'**.

### Classe 'UnitTest'

La classe **'UnitTest'** hérite de la classe **'unittest.TestCase**' et définit les méthodes de test suivantes :

**'setUp()'**

Cette méthode est exécutée avant chaque test et initialise l'instance de la classe **'Sepsis'**, le client de test Flask et le contexte d'application.

**'tearDown()'**

Cette méthode est exécutée après chaque test et nettoie les ressources utilisées.

### Méthodes de test

Le fichier contient plusieurs méthodes de test qui vérifient le bon fonctionnement des fonctions de la classe **'Sepsis'** dans différents scénarios. Les méthodes de test incluent :

- **'test_predict_data_correct()'**
- **'test_predict_data_intcorrect()'**
- **'test_verify_dictionaris_no_containt_string()'**
- **'test_verify_dictionaris_containt_string()'**
- **'test_verify_dictionaris_equals()'**
- **'test_verify_dictionaris_no_equals()'**
- 
Ces tests vérifient les résultats attendus pour différentes entrées de données et conditions.

Ceci conclut la documentation du code backend de l'API.
