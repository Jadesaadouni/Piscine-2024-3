from mongoengine import *
from pymongo import MongoClient

try:
    # Établir une connexion à MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["nobel_database"]  # Créer ou se connecter à la base de données
    print("Connexion réussie avec MongoDB")
except Exception as e:
    print(f"Erreur de connexion avec MongoDB : {e}")
    exit()

connect(db="nobel_database", host="localhost", port=27017)
collection_name = 'nobel_database'
collection = db[collection_name]

def display_countries():
    # Initialisez une liste vide pour stocker les noms de pays
    country_names = []

    # Récupérez les noms de pays à partir de la collection
    for document in collection.find():
        json_data = document.get('countries', {})
        print(json_data)
        
    # Trier les noms des pays par ordre alphabétique
    sorted_country_names = sorted(country_names)

    # Afficher les noms des pays triés
    for country in sorted_country_names:
        print(country)

def display_laureates():
    laureates_list = []
    for document in collection.find():
        json_data = document.get('laureates', {})
        for laureate in json_data:
            firstname = laureate.get('firstname', 'N/A')
            
            laureates_list.append(firstname)
            laureates_list.sort()
    for firstname in laureates_list:
        print(f'firstname: {firstname}')

def display_categories():
    categories_set = set()  # Utilisez un ensemble pour stocker temporairement les catégories

    for document in collection.find():
        categories = document.get('prizes', [])
        for category_data in categories:
            category = category_data.get('category', 'N/A')
            categories_set.add(category)  # Ajoutez la catégorie à l'ensemble

    categories_list = sorted(categories_set)  # Triez les catégories en les convertissant en liste

    # Affichez les catégories triées
    for category in categories_list:
        print(f"Category: {category}")

display_categories() 




