from pydantic import BaseModel

class Lycee(BaseModel):
    nom: str
    ville: str
    commune: str
    departement: str
    type: str
    statut: str
    adresse: str
    code_postal: str
    telephone: str
    latitude: float
    longitude: float
