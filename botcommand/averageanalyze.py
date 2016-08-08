from riotapi import matchlist
from riotapi import match as matchAPI
import threading, queue, time

validRoles = {'SoloTop': {'lane': 'TOP', 'role': 'SOLO'},
              'SoloMid': {'lane': 'MID', 'role': 'SOLO'},
              'Jungle': {'lane': 'JUNGLE', 'role': 'NONE'},
              'SupportBot': {'lane': 'BOT', 'role': 'DUO_SUPPORT'},
              'CarryBot': {'lane': 'BOT', 'role': 'DUO_CARRY'}}

itemsName = ['item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6']
spellsName = ['spell1Id', 'spell2Id']

statsNames = ['kills','deaths','assists','goldEarned','minionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle',
             'sightWardsBoughtInGame','visionWardsBoughtInGame','totalDamageDealtToChampions', 'champLevel']

#DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT

def averageAnalyzeYou(summonerId, region, roles=[], championIds={}, seasons={}, rankedQueues={}, beginTime=-1, endTime=-1, beginIndex=0, endIndex=100, cleanUp=True):
    matchlistjson = matchlist.requestMatchList(summonerId=summonerId, region=region, championIds=championIds, seasons=seasons, rankedQueues=rankedQueues, beginTime=beginTime, endTime=endTime, beginIndex=beginIndex, endIndex=endIndex, cleanUp=cleanUp)

    analyzeRoleDictionary = {}
    for customRole in validRoles:
        analyzeRoleDictionary[customRole] = []
    analyzeRoleDictionary['Non-identifiable'] = []

    for match in matchlistjson['matches']:
        foundRole = False
        for customRole in validRoles.keys():
            if validRoles[customRole]['role'] == match['role'] and validRoles[customRole]['lane'] == match['lane']:
                analyzeRoleDictionary[customRole].append({'matchId': match['matchId'], 'region': match['region']})
                foundRole = True
        if not foundRole:
            analyzeRoleDictionary['Non-identifiable'].append({'matchId': match['matchId'], 'region': match['region']})

    customMatchlist = []

    if roles == []:
        for match in matchlistjson['matches']:
            customMatchlist.append({'matchId': match['matchId'], 'region': match['region']})
    else:
        for role in roles:
            for match in analyzeRoleDictionary[role]:
                customMatchlist.append({'matchId': match['matchId'], 'region': match['region']})


    q = queue.Queue()
    threads = []
    matches = []
    for match in customMatchlist:
        t = threading.Thread(target=matchAPI.requestMatchThreaded, args = (match['matchId'],match['region'],q,))
        t.daemon = True
        t.start()
        time.sleep(0.1)
        threads.append(t)

    for x in threads:
        x.join()

    for i in range(q.qsize()):
        matches.append(q.get())
        if (int(q.qsize()) == 0): break

    cleanMatches = []
    for match in matches:
        if 'status' in match:
            print('FUCKING EW')
        else:
            cleanMatches.append(match)

    matches = cleanMatches

    participantYou = {'items': {}, 'spells': {}, 'champions': {}, 'stats': {}}
    for statName in statsNames: participantYou['stats'][statName] = 0

    #print(participantYou)

    for match in matches:
        championId = getChampionIdBySummonerId(summonerId, match)

        tmp = extractParticipantStatsFromMatch(championId, match)
        participantYou = addParticipantStatsTogether(participantYou, tmp)

    participantYou = averageParticipantStats(participantYou, len(customMatchlist))



    general = {'summonerId': summonerId}


    return (analyzeRoleDictionary, participantYou, general)

def averageParticipantStats(participantStats, factor):
    for stat in participantStats['stats']:
        participantStats['stats'][stat] /= factor
    return participantStats

def extractParticipantStatsFromMatch(championId, matchjson):
    #counter
    itemsCounter = {}
    spellsCounter = {}
    championCounter = {}

    statsSum = {}

    for participant in matchjson['participants']:
        if participant['championId'] == championId:
            #counter
            for itemName in itemsName: itemsCounter[participant['stats'][itemName]] = itemsCounter.get(participant['stats'][itemName], 0) + 1
            for spellName in spellsName: spellsCounter[participant[spellName]] = spellsCounter.get(participant[spellName], 0) + 1

            if participant['championId'] in championCounter:
                championCounter[participant['championId']] = {'count': championCounter[participant['championId']].get('count', 0) + 1, 'wins': 0}
            else:
                championCounter[participant['championId']] = {'count': 1, 'wins': 0}


            for statName in statsNames: statsSum[statName] = statsSum.get(statName, 0) + participant['stats'][statName]

            break

    result = {'items': itemsCounter, 'spells': spellsCounter, 'champions': championCounter, 'stats': statsSum}
    #print(result)

    return result

def addParticipantStatsTogether(participantStatsA, participantStatsB):
    A = participantStatsA['items']
    B = participantStatsB['items']

    itemsTotal = {k: A.get(k, 0) + B.get(k, 0) for k in set(A) | set(B) }

    A = participantStatsA['spells']
    B = participantStatsB['spells']
    spellsTotal = {k: A.get(k, 0) + B.get(k, 0) for k in set(A) | set(B) }

    A = participantStatsA['stats']
    B = participantStatsB['stats']
    statsTotal = {k: A.get(k, 0) + B.get(k, 0) for k in set(A) | set(B) }


    A = participantStatsA['champions']
    B = participantStatsB['champions']
    championsTotal = {k: {'count': A.get(k, {'count': 0}).get('count', 0) + B.get(k, {'count': 0}).get('count', 0),
                          'wins': A.get(k, {'wins': 0}).get('wins', 0) + B.get(k, {'wins': 0}).get('wins', 0)}
                      for k in set(A) | set(B)}

    result = {'items': itemsTotal, 'spells': spellsTotal, 'champions': championsTotal, 'stats': statsTotal}

    return result

def getChampionIdByRole(role):
    print('returns the champion id based on role in match')

def getChampionIdBySummonerId(summonerId, match):
    participantId = -1

    for participantIdentity in match['participantIdentities']:
        if int(participantIdentity['player']['summonerId']) == int(summonerId):
            participantId = participantIdentity['participantId']
            break
    if participantId == -1:
        print('[botcommand/averageanalyze] error in getChampionIdBySummonerId method')
        return

    for participant in match['participants']:
        if int(participant['participantId']) == participantId:
            championId = participant['championId']
            return championId
