import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


class MoyenneModel:
    def predict(self, data):
        return data.mean()


with open('../models/moyenne.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get('/score')
async def get_score():
    df = pd.read_csv('../data/processed/data_test.csv')
    scores = model.predict(df['Notes'])
    return JSONResponse(content={'moyenne': scores.tolist()})
