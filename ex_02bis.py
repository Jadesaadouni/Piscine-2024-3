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

def display_shared_peace_NP():
    shared_prizes = []  # Une liste pour stocker les prix partagés

    # Parcourez les documents de la collection "prizes"
    for document in collection.find():
        prizes = document.get('prizes', [])  # Obtenez la liste des prix du document

        # Parcourez les prix dans le document
        for prize in prizes:
            category = prize.get('category', '')  # Obtenez la catégorie du prix
            laureates = prize.get('laureates', [])  # Obtenez la liste des lauréats

            # Vérifiez si la catégorie est "peace" et s'il y a exactement 2 lauréats
            if category == 'peace' and len(laureates) == 2:
                # Vérifiez si la motivation est la même pour les deux lauréats
                if len(set([laureate.get('motivation') for laureate in laureates])) == 1:
                    shared_prizes.append({
                        'year': prize.get('year', ''),
                        'category': category,
                        'motivation': [f"{laureate.get('motivation')}" for laureate in laureates],  # Incluez la motivation ici
                        'laureates': [f"{laureate.get('firstname')} {laureate.get('surname')}" for laureate in laureates]
                    })

    # Affichez les prix partagés pour la même motivation
    for shared_prize in shared_prizes:
        print(f"Year: {shared_prize['year']}")
        print(f"Category: {shared_prize['category']}")
        print(f"Motivation: {shared_prize['motivation'][0]}")  # Affichez la motivation ici
        print(f"Laureates: {', '.join(shared_prize['laureates'])}")
        print()

#Appelez la fonction pour laffichage
display_shared_peace_NP()