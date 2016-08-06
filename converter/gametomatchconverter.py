from converter import gameconstants

def gameToMatchConverter(game):
    match = {}

    match['matchId'] = game['gameId']
    match['region'] = 'tournament'
    match['platformId'] = game['platformId']
    match['matchMode'] = game['gameMode']
    match['matchType'] = game['gameType']
    match['matchCreation'] = game['gameCreation']
    match['matchDuration'] = game['gameDuration']
    match['queueType'] = gameconstants.queueTypeById[str(game['queueId'])]['nameId']
    match['mapId'] = game['mapId']
    match['season'] = game['seasonId']                  #TODO: Find out correlation between season and seasonId
    match['matchVersion'] = game['gameVersion']
    match['participants'] = game['participants']
    match['participantIdentities'] = game['participantIdentities']
    match['teams'] = game['teams']

    for team in match['teams']:
        if team['win'] == 'Win':
            team['winner'] = True
        elif team['win'] == 'Fail':
            team['winner'] = False
        else:
            print('[converter/gametomatchconverter] Conversion in team failed, this should not happen.')

    for participant in match['participants']:
        try:
            participant['stats']['minionsKilled'] = participant['stats']['totalMinionsKilled']
            participant['stats']['winner'] = participant['stats']['win']
        except:
            print('[converter/gametomatchconverter] Conversion in participant failed, this should not happen.')

    return match