import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = ''
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body = {
        "name" : "Пирожок",
        "photo" : "https://dolnikov.ru/pokemons/albums/040.png"
}

id = '15270'

body_change_name = {
        "pokemon_id" : id,
        "name" : "Ванилька",
        "photo" : "https://dolnikov.ru/pokemons/albums/040.png"
}


body_add = {"pokemon_id" : id}


response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_change_name)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_add)
print(response.text)




