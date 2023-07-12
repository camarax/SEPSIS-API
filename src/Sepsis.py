from flask import jsonify, abort
import pandas as pd
import joblib

class Sepsis:
    
    def __init__(self):
        self.model = None

    def predict(self,model_name,data):
        if self._verify_dictionaris_containt_string(data) == False and self._verify_dictionaris_equals(data) == False:
            # Instanciation du modèle.
            self.model = joblib.load(model_name)
            classe = ["Négatif","Positif"]

            # Conversion de la données en dataFrame
            data = pd.DataFrame([data])

            #Prédiction
            predict = self.model.predict(data)
            predict_proba = self.model.predict_proba(data).tolist()

            # Formatage des resultats
            decimal_proba_list = [format(prob, '.16f') for prob in predict_proba[0]]
            proba = int(float(decimal_proba_list[predict[0]])*100)
            return jsonify({"Prédiction": str(classe[predict[0]]),"Probalité" : str(proba)})
        else:
            # Renvoyer une erreur 422 lrosque les données sont incohérentes
            abort(422,description="Données incorrectes")
           

    def health(self):
        return jsonify({"response" : "Okay"})

    def _verify_dictionaris_containt_string(self,data):
        # verifier si les données sont cohérantes
        for key, value in data.items():
            if isinstance(value,str):
                return True
        return False

    def _verify_dictionaris_equals(self, data):
        if data.keys() != set(["PRG","PL","PR","SK","TS","M11","BD2","Age","Insurance"]):
            return True
        else: 
            return False