from riotapi import champion
from PIL import Image
import requests
from io import BytesIO
from secret.riotapikey import RiotAPIKey

def getSummonerSpellsImages():

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/summoner-spell?api_key=" + RiotAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    data = response['data']

    print(data)

    for name in data:
        templateURL = 'https://ddragon.leagueoflegends.com/cdn/6.14.2/img/spell/{name}.png'
        URL = templateURL.format(name=name)
        response = requests.get(URL)
        img = Image.open(BytesIO(response.content))


        templateSavePath = 'subredditstylesheet/imagesoriginal/{name}.png'
        savePath = templateSavePath.format(name=name)


        img.save(savePath)


