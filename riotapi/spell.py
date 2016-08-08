from secret.riotapikey import RiotAPIKey
from riotapi.apihandler import getJsonFromURL

spellDictionaryById = {}
spellDictionaryByName = {}

def requestSpells():
    print('[riotapi/spell] request spells...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/summoner-spell?api_key=" + RiotAPIKey
    response = getJsonFromURL(URL, 10, 2)

    print('[riotapi/champion] request spell success')

    return response

def updateSpellDictionary():
    response = requestSpells()
    global spellDictionaryById
    global spellDictionaryByName


    data = response['data']
    for spellName in data:
        name = data[spellName]['name'].replace('!','').replace(' ','').lower()

        spellDictionaryByName[name] = data[spellName]['id']
        spellDictionaryById[data[spellName]['id']] = name

