from flask import Flask,jsonify, request, abort
import pandas as pd
from functools import wraps
from flask_swagger_ui import get_swaggerui_blueprint
from Sepsis import Sepsis


app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name' : "Todo list API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)


# ------------------------------------------------------------------------

# Fonction de validation du jeton d'accès
def validate_token(token):
    # Ici, vous pouvez mettre en œuvre votre logique de validation du jeton d'accès
    # Vérifiez si le jeton est valide, non expiré, associé à un utilisateur existant, etc.
    # Pour cet exemple, nous allons simplement vérifier si le jeton est égal à "my_token"
    return token == "lesecret"

# Décorateur pour vérifier le jeton d'accès
def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Récupérer le jeton d'accès à partir de l'en-tête Authorization
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or not validate_token(token):
            abort(401)  # Renvoyer une erreur 401 Unauthorized si le jeton est invalide ou manquant
        return func(*args, **kwargs)
    return wrapper

# ------------------------------------------------------------------------


# Point de terminaison de prediction()
@app.route("/predict", methods=['POST'])
@require_token
def predict():
    ''' Cette fonction prend en parametre les caracteristiques du modèle de l'individu.....
        Params : 
            Data : les caracteris
    '''
    sepsis = Sepsis()
    data = request.get_json()
    return sepsis.predict("model/pipe_modele.model",data)


# Point de terminaison de monitoring
@app.route("/health", methods=['GET'])
@require_token
def health():
    sepsis = Sepsis()
    return sepsis.health()

if __name__ == "__main__":
    app.run(debug=True)
