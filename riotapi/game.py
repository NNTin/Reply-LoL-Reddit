import requests
from converter import gametomatchconverter

def requestGame(matchId, platformId, gameHash, inMatchFormat=True):
    platformId = str(platformId)

    templateURL = 'https://acs.leagueoflegends.com/v1/stats/game/{platformId}/{matchId}?gameHash={gameHash}'

    URL = templateURL.format(platformId=platformId, matchId=matchId, gameHash=gameHash)

    print(URL)

    response = requests.get(URL)
    response.connection.close()
    response = response.json()

    if inMatchFormat:
        return gametomatchconverter.gameToMatchConverter(response)
    else:
        return response

