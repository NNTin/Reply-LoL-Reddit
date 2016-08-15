from secret.riotapikey import RiotAPIKey
from riotapi.apihandler import getJsonFromURL

championDictionaryById = {}
championDictionaryByName = {}

def requestChampions():
    print('[riotapi/champion] request champions...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion?api_key=" + RiotAPIKey
    response = getJsonFromURL(URL, 10, 2)

    print('[riotapi/champion] request champion success')

    return response

def updateChampionDictionary():
    data = requestChampions()
    global championDictionaryById
    global championDictionaryByName

    for championName in data['data']:
        tmpName = data['data'][championName]['name']
        tmpName = tmpName.replace(' ', '')

        championDictionaryById[data['data'][championName]['id']] = tmpName
        championDictionaryByName[tmpName] = data['data'][championName]['id']
