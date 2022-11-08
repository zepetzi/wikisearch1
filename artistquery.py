import requests

query = input('Enter an Artist for a description: \n')

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + f"/artistsearch/{query}")

print(response.json())