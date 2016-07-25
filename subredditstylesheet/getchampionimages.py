from riotapi import champion
from PIL import Image
import requests
from io import BytesIO


def getChampionImages():

    championDictionary = champion.championDictionary(byId=False)

    for name in championDictionary:
        templateURL = 'http://ddragon.leagueoflegends.com/cdn/6.14.2/img/champion/{name}.png'
        URL = templateURL.format(name=name)
        response = requests.get(URL)
        img = Image.open(BytesIO(response.content))


        templateSavePath = 'subredditstylesheet/imagesoriginal/{name}.png'
        savePath = templateSavePath.format(name=name)


        img.save(savePath)
