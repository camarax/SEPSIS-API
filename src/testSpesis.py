import unittest
import pandas as pd
import datetime as dt
from flask import jsonify, abort
from Sepsis import Sepsis
from index import app
from werkzeug.exceptions import UnprocessableEntity

# import sys 
# sys.path.append('/home/camara/Bureau/Cikaba/dash_cast/ETL/')



class UnitTest(unittest.TestCase):

    def setUp(self):
        # initialisation des données d'entrée commmune pour les tests des fonctions de traitement des données passages
        self.sepsis = Sepsis()
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()
       

    def tearDown(self):
        # Nettoyage après le test
        del self.sepsis
        self.ctx.pop()
     


    def test_predict_data_correct(self):
        # Dans le cas où les données sont correctes
        data = {"PRG" : 8,"PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1}
        expected_key = set(["Prédiction","Probalité"])
        # appel de la fonction à tester avec les données d'entrée
        result =self.sepsis.predict("model/pipe_modele.model",data)
        # Vérification du résultat
        self.assertEqual(result.json.keys(), expected_key)
        self.assertEqual(result.status_code,200)

    def test_predict_data_intcorrect(self):
        # Dans le cas ou les données incorrectes
        data = {"PRG" : "string","PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1}
        try:
            result = self.sepsis.predict("model/pipe_modele.model",data)
            self.fail("Expected UnpressableEntity exception")
        except UnprocessableEntity as e:
            self.assertEqual(str(e), "422 Unprocessable Entity: Données incorrectes")


    def test_verify_dictionaris_no_containt_string(self):
        # Dans le cas ou le docuemnt ne contient pas de chaine de caractère
        data = {"PRG" : 8,"PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1}
        self.assertFalse(self.sepsis._verify_dictionaris_containt_string(data))

    def test_verify_dictionaris_containt_string(self):
        # dans le cas ou le document contient une chaine de caractères
        data = {"PRG" : "string","PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1}
        result = self.sepsis._verify_dictionaris_containt_string(data)
        self.assertTrue(result)

    def test_verify_dictionaris_equals(self):
        # Dans le cas ou les clefs sont identiques
        data = {"PRG" : 8,"PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1}
        self.assertFalse(self.sepsis._verify_dictionaris_equals(data))

    def test_verify_dictionaris_no_equals(self):
        # Dans le cas ou les clefs sont ne sont pas identiques
        data = {"PRG" : 8,"PL" : 183,"PR" : 64,"SK" : 0,"TS" : 0,"M11" : 23.3,"BD2" : 0.672,"Age" : 32,"Insurance" : 1,"autre":78}
        self.assertTrue(self.sepsis._verify_dictionaris_equals(data))

