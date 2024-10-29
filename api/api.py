import dill as pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Définir la classe MoyenneModel ici
class MoyenneModel:
    def predict(self, data):
        return data.mean()

# Charger le modèle
with open('../models/moyenne.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get('/')
async def read_root():
    return {"message": "Bienvenue à l'API de calcul de moyenne!"}

@app.get('/score')
async def get_score():
    df = pd.read_csv('../data/processed/data_test.csv')
    scores = model.predict(df['Notes'])
    return JSONResponse(content={'moyenne': scores.tolist()})
