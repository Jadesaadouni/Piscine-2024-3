from mongoengine import *

from pymongo import MongoClient

#Établir la connexion à MongoDB sur localhost et le port par défaut (27017)

client = MongoClient("localhost", 27017)

try:
    # Créer une nouvelle base de données appelée "nobel_database"
    db = client["nobel_database"]
    print("Connexion réussie avec MongoDB")
except Exception as e:
    print(f"Erreur de connexion avec MongoDB : {e}")
    exit()


connect(db='nobel_database', host='localhost', port=27017)

class Prix(Document):
    montant = FloatField(required=True)

from mongoengine import Document, StringField, IntField, ReferenceField, ListField

class Personne(Document):
    prenom = StringField(required=True)

from mongoengine import Document, StringField

class Pays(Document):
    nom = StringField(required=True, unique=True)

from mongoengine import Document, StringField

class Affiliation(Document):
    nom = StringField(required=True, unique=True)

from mongoengine import Document, StringField

class Categorie(Document):
    nom = StringField(required=True, unique=True)