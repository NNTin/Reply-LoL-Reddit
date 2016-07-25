import requests
from secret.riotapikey import RiotAPIKey

championDictionaryById = {}
championDictionaryByName = {}

def requestChampions():
    print('[riotapi/champion] request champions...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion?api_key=" + RiotAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    print('[riotapi/champion] request champion success')

    return response

def updateChampionDictionary():
    data = requestChampions()
    global championDictionaryById
    global championDictionaryByName

    for championName in data['data']:
        championDictionaryById[data['data'][championName]['id']] = championName
        championDictionaryByName[championName] = data['data'][championName]['id']
