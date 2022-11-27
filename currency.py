import requests
import json
API_KEY = 'fa5dec1241aa18580ecb2909'
# Where USD is the base currency you want to use
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

response = requests.get(f'{url}').json()


currencies = dict(response['conversion_rates'])










