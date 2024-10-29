# tests/test_api.py

from fastapi.testclient import TestClient
from api.api import app
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue à l'API de calcul de moyenne!"}

def test_get_score_valid():
    response = client.get("/score")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['moyenne'], list)  # Vérifier que la moyenne est une liste

def test_get_score_empty_dataset(mocker):
    # Mocker la lecture du fichier pour simuler un dataset vide
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame(columns=['Élève', 'Notes']))
    response = client.get("/score")
    assert response.status_code == 200
    data = response.json()
    assert data['moyenne'] == []  # Vérifiez que la moyenne renvoyée est vide

def test_get_score_invalid_endpoint():
    response = client.get("/invalid")
    assert response.status_code == 404  # Vérifiez que l'endpoint inexistant renvoie une erreur 404

def test_predict_exception():
    # Exemple d'une fonction qui pourrait lever une exception
    with pytest.raises(ValueError):
        model = MoyenneModel()
        model.predict(None)  # Simule une entrée invalide
