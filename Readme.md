# Projet API Lycées Numériques 🚀

## Présentation du Projet

Ce projet a été réalisé dans le cadre d’un TP de ARCHI web en Master 2.  
L’objectif est de créer une API REST complète pour gérer des données publiques, les stocker dans une base MongoDB, les afficher via un frontend, et dockeriser l’ensemble.

---

## Dataset utilisé 📊

- Dataset : [Liste des Lycées Français](https://www.data.gouv.fr/fr/datasets/lycees-francais/)  
- Source : data.gouv.fr  
- Format : CSV  

### Pourquoi ce choix ?
J'ai choisi ce dataset car :
- Il est bien structuré (CSV clair)
- Il contient des informations intéressantes sur les établissements scolaires (nom, adresse, région...)
- Les données sont pertinentes pour des recherches, des filtres et des analyses statistiques.

---

## Fonctionnalités du Projet 🎯

## Stack Technique 🖥️

- Python 3.11
- FastAPI
- MongoDB
- Docker / Docker-Compose
- Pymongo
- Pandas
- Uvicorn

### Backend API (FastAPI - Python)

Routes disponibles :
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET     | `/` | Accueil de l'API |
| GET     | `/donnees` | Liste complète des lycées |
| GET     | `/donnees/{index}` | Obtenir un lycée par son index |
| GET     | `/donnees/by_name/{nom}` | Rechercher un lycée par son nom |
| GET     | `/donnees_filtrees?region=NomRegion` | Filtrer les lycées par région |
| POST    | `/reload_csv` | Recharger les données depuis le CSV vers MongoDB |

---

## Installation et Lancement du Projet 🚀

1. Cloner le dépôt :
```bash
git clone https://github.com/Fouad-berry/TP-DOCKER-GROUP.git
cd TP-DOCKER-GROUP
