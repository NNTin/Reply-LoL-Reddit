from converter import gametomatchconverter
from riotapi.apihandler import getJsonFromURL

def requestGame(matchId, platformId, gameHash, inMatchFormat=True):
    platformId = str(platformId)

    templateURL = 'https://acs.leagueoflegends.com/v1/stats/game/{platformId}/{matchId}?gameHash={gameHash}'

    URL = templateURL.format(platformId=platformId, matchId=matchId, gameHash=gameHash)

    print(URL)

    response = getJsonFromURL(URL, 10, 2)

    if inMatchFormat:
        return gametomatchconverter.gameToMatchConverter(response)
    else:
        return response

