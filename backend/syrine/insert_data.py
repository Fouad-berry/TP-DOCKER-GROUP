import pandas as pd
from database import collection  # Assurez-vous que 'collection' est bien défini dans 'database.py'

df = pd.read_csv("lycee.csv", sep=";")

for _, row in df.iterrows():
    try:
        doc = {
            "nom": row["OR_PATRONYME"],
            "ville": row["OR_VILLE"],
            "commune": row["commune"],
            "departement": row["département"],
            "type": row["Type"],
            "statut": row["statut"],
            "adresse": row["adresse"],
            "code_postal": row["CP"],
            "telephone": row["téléphone"],
            "latitude": float(str(row["latitude (Y)"]).replace(",", ".")),
            "longitude": float(str(row["longitude (X)"]).replace(",", "."))
        }
        collection.insert_one(doc)
    except Exception as e:
        print(f"Erreur sur la ligne {row}: {e}")  # Affiche les erreurs avec les données concernées

print("✅ Insertion terminée !")
