import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'advertisement':10, 'airplay':43, 'brand':10})

print(r.json())