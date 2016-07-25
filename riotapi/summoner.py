import requests
from secret.riotapikey import RiotAPIKey
from riotapi.validparameters import validRegions

def requestSummoner(summoners, region, byID=True):
    region = str(region).lower()
    if region not in validRegions:
        print('[riotapi/summoner] %s is not a valid region' %region)
        return

    templateURLSummonersID = 'https://{region}.api.pvp.net/api/lol/{region}/v1.4/summoner/{summoners}?api_key=' + RiotAPIKey
    templateURLSummonersName = 'https://{region}.api.pvp.net/api/lol/{region}/v1.4/summoner/by-name/{summoners}?api_key=' + RiotAPIKey

    templateURL = ''
    if byID == True:
        templateURL = templateURLSummonersID
    else:
        templateURL = templateURLSummonersName

    summoners = formatDict(summoners)

    URL = templateURL.format(region=region, summoners=summoners)


    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    return response

def formatDict(input):
    output = ''
    for value in input:
        output += str(value) + ','
    return output[:-1]