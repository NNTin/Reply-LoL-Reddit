from secret.riotapikey import RiotAPIKey
from riotapi.apihandler import getJsonFromURL

itemDictionary = {}

def requestItems():
    print('[riotapi/item] request items...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item?api_key=" + RiotAPIKey
    response = getJsonFromURL(URL, 10, 2)

    print('[riotapi/champion] request item success')

    return response

def updateItemDictionary():
    response = requestItems()
    global itemDictionary

    data = response['data']
    for itemId in data:
        if 'name' in data[itemId]:
            itemDictionary[itemId] = data[itemId]['name']

