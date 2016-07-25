#https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=RGAPI-9B0F1DDB-53F4-4B10-935B-9AC8BAF7D1D8

import requests
from secret.riotapikey import RiotAPIKey

itemDictionary = {}

def requestItems():
    print('[riotapi/item] request items...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=" + RiotAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    print('[riotapi/champion] request item success')

    return response

def updateItemDictionary():
    response = requestItems()
    global itemDictionary

    data = response['data']
    for itemId in data:
        if 'name' in data[itemId]:
            itemDictionary[itemId] = data[itemId]['name']

