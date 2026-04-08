import requests

paikkakunta = input("Anna paikkakunnan nimi: ")
api_avain = "0a40f33f698cc03c9a5a51aa7bd97f43"

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&lang=fi").json()

lampotila = data["main"]["temp"] - 273.15
saatila = data["weather"][0]["description"]

print(f"Säätila: {saatila}")
print(f"Lämpötila: {lampotila:.1f} °C")
