from riotapi import champion
from PIL import Image
import requests
from io import BytesIO
from secret.riotapikey import RiotAPIKey

def getItemImages():

    #https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=RGAPI-9B0F1DDB-53F4-4B10-935B-9AC8BAF7D1D8



    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=" + RiotAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()



    for id in response['data']:
        templateURL = 'https://ddragon.leagueoflegends.com/cdn/6.14.2/img/item/{id}.png'
        URL = templateURL.format(id=str(id))
        response = requests.get(URL)
        img = Image.open(BytesIO(response.content))


        templateSavePath = 'subredditstylesheet/imagesoriginal/{id}.png'
        savePath = templateSavePath.format(id=str(id))


        img.save(savePath)
