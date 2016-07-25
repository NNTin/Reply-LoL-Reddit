import requests
from secret.riotapikey import RiotAPIKey
from riotapi.validparameters import validSeasons, validRankedQueues, validRegions

def requestMatchList(summonerId, region, championIds={}, seasons={}, rankedQueues={}, beginTime=-1, endTime=-1, beginIndex=-1, endIndex=-1):
    region = str(region).lower()
    if region not in validRegions:
        print('[riotapi/summoner] %s is not a valid region' %region)
        return
    additionalSearchParameters = ''
    if dictIsNotEmpty(championIds):
        championIds = formatDict(championIds)
        additionalSearchParameters += '&championIds=' + championIds
    if dictIsNotEmpty(seasons):
        if isValidDict(seasons, validSeasons):
            seasons = formatDict(seasons)
            additionalSearchParameters += '&seasons=' + seasons
        else:
            print('[riotapi/matchlist] invalid seasons parameters was given, should not happen')
    if dictIsNotEmpty(rankedQueues):
        if isValidDict(rankedQueues, validRankedQueues):
            rankedQueues = formatDict(rankedQueues)
            additionalSearchParameters += '&rankedQueues=' + rankedQueues
        else:
            print('[riotapi/matchlist] invalid rankedQueues parameters was given, should not happen')

    if beginTime is not -1:
        if isinstance(beginTime, int) and beginTime > 0:
            additionalSearchParameters += '&beginTime=' + str(beginTime)
        else:
            print('[riotapi/matchlist] invalid beginTime parameter was given, should not happen')

    if beginTime is not -1:
        if isinstance(endTime, int) and endTime > 0:
            additionalSearchParameters += '&endTime=' + str(endTime)
        else:
            print('[riotapi/matchlist] invalid endTime parameter was given, should not happen')

    if beginTime is not -1:
        if isinstance(beginIndex, int) and beginIndex > 0:
            additionalSearchParameters += '&beginIndex=' + str(beginIndex)
        else:
            print('[riotapi/matchlist] invalid beginIndex parameter was given, should not happen')

    if beginTime is not -1:
        if isinstance(endIndex, int) and endIndex > 0:
            additionalSearchParameters += '&endIndex=' + str(endIndex)
        else:
            print('[riotapi/matchlist] invalid endIndex parameter was given, should not happen')


    templateURL = 'https://{region}.api.pvp.net/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}?api_key=' + RiotAPIKey + additionalSearchParameters

    URL = templateURL.format(region=region, summonerId=summonerId)

    print(URL)

    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    return response


def dictIsNotEmpty(dict):
    return bool(dict)

def formatDict(input):
    output = ''
    for value in input:
        output += str(value) + ','
    return output[:-1]

def isValidDict(dict, validDict):
    for value in dict:
        if value not in validDict:
            return False
    return True