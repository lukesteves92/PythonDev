import requests

url = 'https://api.exchangerate.host/latest'

payload = {'base': 'USD'}

r = requests.get(url, params=payload)

print(r.text)

