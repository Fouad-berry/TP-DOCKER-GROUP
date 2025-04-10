from fastapi import FastAPI
import pandas as pd
from mongo import collection
from bson import ObjectId  # Import pour gérer les _id MongoDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# 🔁 Fonction utilitaire pour lire le CSV
def lire_csv():
    df = pd.read_csv("lycees.csv", on_bad_lines="skip", sep=";")
    return df.fillna("").to_dict(orient="records")


# 🔁 Fonction utilitaire pour convertir les ObjectId en string
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


# 🔄 Initialisation (une seule fois si Mongo est vide)
if collection.count_documents({}) == 0:
    print("Chargement initial depuis CSV vers MongoDB")
    collection.insert_many(lire_csv())


# ✅ Accueil
@app.get("/")
def home():
    return {
        "message du Groupe TP-DOCKER-GROUP":
        "Bienvenue sur l’API des lycées numériques ; ajoutez un /docs pour visualiser le contenu"
    }


# 📚 Route principale : données Mongo (ou CSV via ?source=csv)
@app.get("/donnees")
def get_all(source: str = "mongo"):
    if source == "csv":
        return lire_csv()
    data = list(collection.find({}))
    return [serialize_doc(doc) for doc in data]


# 🔍 Accès par index
@app.get("/donnees/{index}")
def get_one(index: int, source: str = "mongo"):
    data = lire_csv() if source == "csv" else list(collection.find({}))
    data = [serialize_doc(doc) for doc in data] if source == "mongo" else data
    if 0 <= index < len(data):
        return data[index]
    return {"error": "Index invalide"}


# 🔎 Recherche par nom
@app.get("/donnees/by_name/{nom}")
def get_by_name(nom: str, source: str = "mongo"):
    data = lire_csv() if source == "csv" else list(collection.find({}))
    data = [serialize_doc(doc) for doc in data] if source == "mongo" else data
    results = [d for d in data if d.get("OR_PATRONYME", "").lower() == nom.lower()]
    return results or {"error": "Aucun lycée trouvé avec ce nom"}


# 🔎 Filtrage par région
@app.get("/donnees_filtrees")
def get_filtre(region: str = None, source: str = "mongo"):
    data = lire_csv() if source == "csv" else list(collection.find({}))
    data = [serialize_doc(doc) for doc in data] if source == "mongo" else data
    if region:
        return [d for d in data if str(d.get("region", "")).lower() == region.lower()]
    return {"message": "Utilise ?region=NomDeLaRégion"}


# 🔁 Rechargement complet depuis CSV vers Mongo
@app.post("/reload_csv")
def reload_csv():
    data = lire_csv()
    collection.delete_many({})
    collection.insert_many(data)
    return {"status": "MongoDB vidé et rechargé avec lycees.csv ✅"}

