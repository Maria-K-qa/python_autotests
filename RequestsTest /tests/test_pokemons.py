import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f6ecc30cdefb97bdf8fb67f1d70fde25'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4384'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Манчоус' 

