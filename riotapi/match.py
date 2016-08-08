from secret.riotapikey import RiotAPIKey
from riotapi.validparameters import validRegions
from riotapi.apihandler import getJsonFromURL


def requestMatch(matchId, region, includeTimeline=False):
    region = str(region).lower()
    if region not in validRegions:
        print('[riotapi/match] %s is not a valid region' %region)
        return

    additionalSearchParameters = '&includeTimeLine=' + str(includeTimeline)

    templateURL = 'https://{region}.api.pvp.net/api/lol/{region}/v2.2/match/{matchId}?api_key=' + RiotAPIKey + additionalSearchParameters

    URL = templateURL.format(region=region, matchId=matchId )

    print(URL)

    return getJsonFromURL(URL, 5)



def requestMatchThreaded(matchId, region, q, includeTimeLine=False):
    result = requestMatch(matchId=matchId, region=region, includeTimeline=includeTimeLine)
    q.put(result)