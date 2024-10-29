# tests/test_api.py

from fastapi.testclient import TestClient
from api.api import app
import pytest

client = TestClient(app)

def test_read_root():#Tests de Valeur, Vérifie que la racine de l'API renvoie le bon message et le code de statut 200.
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue à l'API de calcul de moyenne!"}

def test_get_score_valid(): #Tests de Valeur, Vérifie que l'API renvoie un code de statut 200 et que le format de la réponse est correct (une liste pour la moyenne).
    response = client.get("/score")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['moyenne'], list)  # Vérifier que la moyenne est une liste

def test_get_score_empty_dataset(mocker):#Tests d'État simule un DataFrame vide et vérifie que la réponse renvoie une liste vide.
    # Mocker la lecture du fichier pour simuler un dataset vide
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame(columns=['Élève', 'Notes']))
    response = client.get("/score")
    assert response.status_code == 200
    data = response.json()
    assert data['moyenne'] == []  # Vérifiez que la moyenne renvoyée est vide

def test_get_score_invalid_endpoint():#Tests d'État, vérifie qu'une requête à un endpoint inexistant renvoie une erreur 404.
    response = client.get("/invalid")
    assert response.status_code == 404  # Vérifiez que l'endpoint inexistant renvoie une erreur 404

def test_predict_exception():# Test d'exception, vérifie qu'une exception est levée si le modèle reçoit des données invalides (comme None).
    # Exemple d'une fonction qui pourrait lever une exception
    with pytest.raises(ValueError):
        model = MoyenneModel()
        model.predict(None)  # Simule une entrée invalide
