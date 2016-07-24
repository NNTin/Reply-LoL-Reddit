import requests
#message = True

SteamAPIKey = "RGAPI-9B0F1DDB-53F4-4B10-935B-9AC8BAF7D1D8"


def requestChampions():
    print('[riotapi/champion] request champions...')

    URL = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion?api_key=" + SteamAPIKey
    response = requests.get(URL)
    response.connection.close()
    response = response.json()


    print('[riotapi/champion] request champion success')

    return response

def championDictionary(byId=False):
    data = requestChampions()
    dictionary = {}
    for championName in data['data']:
        if byId == True:
            dictionary[data['data'][championName]['id']] = championName
        else:
            dictionary[championName] = data['data'][championName]['id']
    return dictionary
