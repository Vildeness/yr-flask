import requests

def hent_temp(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    respons = requests.get(url, headers={"User-agent": "Vildes mac"})
    data = respons.json()
    tempratur = data["properties"]["timeseries"][0] ["data"] ["instant"] ["details"] ["air_temperature"]