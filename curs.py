import requests
import json

r = requests.get('https://www.cbr-xml-daily.ru/latest.js')
texts = json.loads(r.content)
Rates = texts.get('rates')
#print(Rates)

USD = str(Rates.get('USD'))
print(USD)
