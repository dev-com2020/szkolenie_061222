import requests

respone = requests.get("http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Kielce&aqi=no")
print(respone.status_code)
plik = respone.json()['location']['name']
print(plik)