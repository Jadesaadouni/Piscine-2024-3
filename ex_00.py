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
