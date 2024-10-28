from flask import Flask, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Chargement du modèle
with open('models/moyenne.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/score', methods=['GET'])
def get_score():
    df = pd.read_csv('data/processed/data_test.csv')
    scores = model.predict(df['Notes'])
    return jsonify({'moyenne': scores})

if __name__ == '__main__':
    # host='0.0.0.0' : Cela permet à l'application d'écouter sur toutes les interfaces réseau, 
    # ce qui est nécessaire pour permettre l'accès externe à l'API.
    app.run(debug=True, host='0.0.0.0', port=5000) #port=5000 : Définit le port sur lequel l'application API écoutera
