from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("lycees.csv", on_bad_lines="skip", sep=";")
donnees = df.to_dict(orient="records")

@app.get("/")
def home():
    return {"message": "Bienvenue sur l’API des lycées numériques"}

@app.get("/donnees")
def get_all():
    return donnees

@app.get("/donnees/{index}")
def get_one(index: int):
    if 0 <= index < len(donnees):
        return donnees[index]
    return {"error": "Index invalide"}

@app.get("/donnees_filtrees")
def get_filtre(region: str = None):
    if region:
        results = [d for d in donnees if str(d.get("region", "")).lower() == region.lower()]
        return results
    return {"message": "Utilise ?region=NomDeLaRégion"}