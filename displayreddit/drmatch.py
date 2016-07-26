from converter import championconverter, itemconverter, spellconverter, timeconverter, matchconverter
from converter.timeconverter import unixTimeConverter, durationTimeConverter

def drMatch(matchjson):
    print(matchjson)

    matchId = matchjson['matchId']
    matchType = matchconverter.matchType[matchjson['matchType']]
    matchMode = matchconverter.matchMode[matchjson['matchMode']]
    queueType = matchconverter.queueType[matchjson['queueType']]
    season = matchconverter.season[matchjson['season']]

    matchCreation = unixTimeConverter(matchjson['matchCreation'])
    matchDuration = durationTimeConverter(matchjson['matchDuration'])

    participantIdentities = matchjson['participantIdentities']
    participants = matchjson['participants']
    teams = matchjson['teams']

    for participantId in range(0, len(participantIdentities)):
        participants[participantId]['player'] = participantIdentities[participantId]['player']



    tableBody = ''
    firstRun = True
    for team in teams:
        table = ''
        if firstRun:
            table = 'Lvl | C | Name | Spells | K/D/A | ItemsItemsItems | Farm | Creeps | S/V | Damage\n' \
                ':-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:\n'
            templateTable = '{level} | {champion} | {name} | {spells} | {kda} | {items} | {farm} | {creeps} | {wards} | {damage}\n'
            firstRun = False
        else:
            table = '-|-|-|-|-|-|-|-|-|-|-\n'

        for participant in participants:
            if participant['teamId'] == team['teamId']:
                level = str(participant['stats']['champLevel'])
                champion = championconverter.championConverter[participant['championId']]
                name = participant['player']['summonerName']

                spells  = spellconverter.spellConverter[participant['spell1Id']]
                spells += spellconverter.spellConverter[participant['spell2Id']]
                kda = '%s/%s/%s' %(participant['stats']['kills'],participant['stats']['deaths'],participant['stats']['assists'])

                #TODO: Implement else. Check why some item ids do not exist in itemConverter (e.g. 1331)
                items = ''
                if str(participant['stats']['item0']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item0'])]
                if str(participant['stats']['item1']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item1'])]
                if str(participant['stats']['item2']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item2'])]
                if str(participant['stats']['item3']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item3'])]
                if str(participant['stats']['item4']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item4'])]
                if str(participant['stats']['item5']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item5'])]
                if str(participant['stats']['item6']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item6'])]

                farm = participant['stats']['goldEarned']
                creeps = participant['stats']['minionsKilled'] + participant['stats']['neutralMinionsKilledTeamJungle'] + participant['stats']['neutralMinionsKilledEnemyJungle']
                wards = '%s/%s' %(participant['stats']['sightWardsBoughtInGame'], participant['stats']['visionWardsBoughtInGame'])
                damage = participant['stats']['totalDamageDealtToChampions']

                table += templateTable.format(level=level, champion=champion, name=name, spells=spells, kda=kda, items=items, farm=farm, creeps=creeps, wards=wards, damage=damage)
        tableBody += table


    #matchId matchType queueType season matchCreation

    #introTemplate = 'Match ID: {matchId}; match type: {matchType}; match mode: {matchMode}, queue type: {queueType}; match creation date: {matchCreation}; match duration: {matchDuration}\n\n'
    #intro = introTemplate.format(matchId=matchId, matchType=matchType, matchMode=matchMode, queueType=queueType, matchCreation=matchCreation, matchDuration=matchDuration)

    #print(intro)

    #the wings gaming WINS 27-35 @ 50 minutes

    #TODO: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    introTemplate = '[**{teamWinner} wins {blueKills}-{purpleKills} @ {matchDuration}**](/#spoiler "Match ID: {matchId}; match type: {matchType}; match mode: {matchMode}, queue type: {queueType}; match creation date: {matchCreation}; match duration: {matchDuration}")\n\n'
    print(introTemplate)
