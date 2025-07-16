import requests

MY_LAT = 25.204849
MY_LNG = 55.270782

par = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 1}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=par)
response.raise_for_status()

sunrise = response.json()
sunset = response.json()

MY_POS = (sunrise, sunset)

print(MY_POS)
