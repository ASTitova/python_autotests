import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '7e665bda84485b4bff148440ddde5d82'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level' : 1})
    assert response.status_code == 200 

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 2195})
    assert response.json()['data'][0]['trainer_name'] == 'Тито'