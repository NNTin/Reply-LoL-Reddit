import requests
from secret.riotapikey import RiotAPIKey
from riotapi.validparameters import validRegions


def requestMatch(matchId, region, includeTimeline=False):
    region = str(region).lower()
    if region not in validRegions:
        print('[riotapi/summoner] %s is not a valid region' %region)
        return

    additionalSearchParameters = '&includeTimeLine=' + str(includeTimeline)

    templateURL = 'https://{region}.api.pvp.net/api/lol/{region}/v2.2/match/{matchId}?api_key=' + RiotAPIKey + additionalSearchParameters

    URL = templateURL.format(region=region, matchId=matchId )

    print(URL)

    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    return response
