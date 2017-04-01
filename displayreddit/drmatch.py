from converter import championconverter, itemconverter, spellconverter, timeconverter, gameconstants
from converter.timeconverter import unixTimeConverter, durationTimeConverter

hoverToView = False

def drMatch(matchjson):
    region = matchjson['region']
    matchId = matchjson['matchId']
    matchType = gameconstants.matchType[matchjson['matchType']]
    matchMode = gameconstants.matchMode[matchjson['matchMode']]
    queueType = gameconstants.queueTypeByName[matchjson['queueType']]['name']
    #season = gameconstants.season[matchjson['season']]             #TODO: solve gametomatchconverter.py first!

    matchCreation = unixTimeConverter(matchjson['matchCreation'])
    matchDuration = durationTimeConverter(matchjson['matchDuration'])

    teamWinner = ''
    blueKills = 0
    purpleKills = 0

    participantIdentities = matchjson['participantIdentities']
    participants = matchjson['participants']
    teams = matchjson['teams']


    playerMissing = False
    for participantId in range(0, len(participantIdentities)):
        if 'player' in participantIdentities[participantId].keys():
            participants[participantId]['player'] = participantIdentities[participantId]['player']
        else:
            playerMissing = True



    tableBody = ''
    firstRun = True
    for team in teams:

        for participant in participants:
            if participant['teamId'] == team['teamId']:

                if firstRun:
                    blueKills += participant['stats']['kills']
                else:
                    purpleKills += participant['stats']['kills']

        table = ''
        if firstRun:

            table = 'Lvl | C | Name | Spells | K/D/A | Items | Gold | Creeps | Wards | Damage\n' \
                ':-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:\n'
            templateTable = '{level} | {champion} | {name} | {spells} | {kda} | {items} | {gold} | {creeps} | {wards} | {damage}\n'
            firstRun = False
            if playerMissing:
                table = 'Lvl | C | Spells | K/D/A | Items | Gold | Creeps | Wards | Damage\n' \
                ':-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:\n'
                templateTable = '{level} | {champion} | {spells} | {kda} | {items} | {gold} | {creeps} | {wards} | {damage}\n'
            if team['winner']:
                teamWinner = 'Blue'
            else:
                teamWinner = 'Red'



        else:
            table = '-|-|-|-|-|-|-|-|-|-|-\n'

        for participant in participants:
            if participant['teamId'] == team['teamId']:
                level = str(participant['stats']['champLevel'])
                champion = championconverter.championConverter[participant['championId']]

                name = ''
                if not playerMissing:
                    name = participant['player']['summonerName']

                spells = ''
                if participant['spell1Id'] in spellconverter.spellConverter.keys():
                    spells += spellconverter.spellConverter[participant['spell1Id']]
                else:
                    spells += str(participant['spell1Id'])
                if participant['spell2Id'] in spellconverter.spellConverter.keys():
                    spells += spellconverter.spellConverter[participant['spell2Id']]
                else:
                    spells += str(participant['spell2Id'])


                kda = '%s/%s/%s' %(participant['stats']['kills'],participant['stats']['deaths'],participant['stats']['assists'])

                #TODO: Implement else. Check why some item ids do not exist in itemConverter (e.g. 1331)
                items = ''
                if str(participant['stats']['item0']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item0'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item0']))
                if str(participant['stats']['item1']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item1'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item1']))
                if str(participant['stats']['item2']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item2'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item2']))
                if str(participant['stats']['item3']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item3'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item3']))
                if str(participant['stats']['item4']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item4'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item4']))
                if str(participant['stats']['item5']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item5'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item5']))
                if str(participant['stats']['item6']) in itemconverter.itemConverter: items += itemconverter.itemConverter[str(participant['stats']['item6'])]
                #else: print('Item ID not found: ' + str(participant['stats']['item6']))

                gold = participant['stats']['goldEarned']
                creeps = participant['stats']['minionsKilled'] + participant['stats']['neutralMinionsKilledTeamJungle'] + participant['stats']['neutralMinionsKilledEnemyJungle']
                wards = '%s' %(participant['stats']['sightWardsBoughtInGame'] + participant['stats']['visionWardsBoughtInGame'])
                damage = participant['stats']['totalDamageDealtToChampions']

                table += templateTable.format(level=level, champion=champion, name=name, spells=spells, kda=kda, items=items, gold=gold, creeps=creeps, wards=wards, damage=damage)


        tableBody += table


    introTemplate = ''
    if hoverToView: introTemplate += '####&#009;\n#####&#009; Hover to view match ID: {matchId} played on {region}\n######&#009;\n'
    introTemplate += '[**{teamWinner} wins {blueKills}-{purpleKills} @ {matchDuration}**](/#spoiler "Match ID: {matchId}; match type: {matchType}; match mode: {matchMode}, queue type: {queueType}; match creation date: {matchCreation}; match duration: {matchDuration}; region: {region}")\n\n'

    intro = introTemplate.format(region=region, teamWinner=teamWinner, blueKills=blueKills, purpleKills=purpleKills, matchId=matchId, matchType=matchType, matchMode=matchMode, queueType=queueType, matchCreation=matchCreation, matchDuration=matchDuration)

    message = '###A letter from Lumbdi, creator of Reply-LoL-Reddit\n\n' \
    '/r/leagueoflegends Visitor,\n\n' \
    'Some of you may know me; many of you probably won’t these days. This bot was born on July 24th, 2016. It was a mere 2 months after I turned 18, and it was the second bot I’d ever made. [/u/Reply-Dota-2-Reddit](https://www.reddit.com/r/dota2/user/Reply-Dota-2-Reddit) was the first bot (before /u/analyzelast100games), Reddit had no bots and maybe 5% of the Redditors that it does today.\n\n'\
    '[...]\n\n' \
    'In the meantime, I hope some of you will join me and over 50 thousand other players for a game of /r/place (it’s free!)\n\n'

    return (message)
