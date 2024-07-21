import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f6ecc30cdefb97bdf8fb67f1d70fde25'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "КотБегемот",
    "photo_id": 143
}

body_rename = {
    "pokemon_id": "44217",
    "name": "Васька",
    "photo_id": 143
    }

body_pokeball = {
    "pokemon_id": "44217"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)