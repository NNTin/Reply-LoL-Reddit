import requests
from secret.riotapikey import RiotAPIKey


def requestSummoner(region=None, byID=True, input={}):
    if region == None:
        print('[riotapi/summoner] specify a region!')
        return

    validRegions = {'br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'ru', 'tr'}
    region = str(region).lower()
    if region not in validRegions:
        print('[riotapi/summoner] %s is not a valid region' %region)
        return

    if input == {}:
        print('[riotapi/summoner] no input found (summoner name or id)')
        return

    templateURLSummonerID = 'https://{region}.api.pvp.net/api/lol/{region}/v1.4/summoner/{input}?api_key=' + RiotAPIKey
    templateURLSummonerName = 'https://{region}.api.pvp.net/api/lol/{region}/v1.4/summoner/by-name/{input}?api_key=' + RiotAPIKey

    templateURL = ''
    if byID == True:
        templateURL = templateURLSummonerID
    else:
        templateURL = templateURLSummonerName

    formattedInput = ''
    for value in input:
        formattedInput += str(value) + ','
    formattedInput = formattedInput[:-1]

    URL = templateURL.format(region=region, input=formattedInput)
    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    return response