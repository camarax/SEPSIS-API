from flask import Flask,jsonify, request, abort
import pandas as pd
from functools import wraps

# import du model
import joblib
model = joblib.load('model/pipe_modele.model')


app = Flask(__name__)


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
        token = request.headers.get('Authorization')
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
    classe = ["Négatif","Positif"]
    data = request.get_json()
    # # 0. Conversion du fichier json en dataFrame
    data = pd.DataFrame([data])

    # # 2. Estimation du modèle
    predict = model.predict(data)
    predict_proba = model.predict_proba(data).tolist()


    decimal_proba_list = [format(prob, '.16f') for prob in predict_proba[0]]
    proba = int(float(decimal_proba_list[predict[0]])*100)

    # # 3. Renvoie du resultat
    return jsonify({"Prédiction": str(classe[predict[0]]),"Probalité" : str(proba)})


# Point de terminaison de monitoring
@app.route("/health", methods=['GET'])
@require_token
def health():
    return jsonify({"response" : str(200)})

if __name__ == "__main__":
    app.run(debug=True)
