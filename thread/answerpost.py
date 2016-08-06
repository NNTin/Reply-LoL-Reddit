import re, time
from riotapi import match, game
from displayreddit import drmatch, drouttro


def analyzePost(post):
    #Checking for match id link
    patternsMatch = ['matchhistory\.(?P<region>\w+)\.leagueoflegends\.(?P<domain>\w+)/(?P<language>\w+)/#match-details/(?P<region2>\w+)/(?P<matchid>\w+)', #leagueoflegends.com
            'lolking.net/summoner/(?P<region>\w+)/(?P<playerid>\w+)#matches/(?P<matchid>\w+)', #lolking.net
            'lolskill.net/match/(?P<region>\w+)/(?P<matchid>\w+)'] #lolskill.net

    for pattern in patternsMatch:
        patternMatch = re.search(pattern, post.body, re.I)
        if patternMatch != None:
            linkToComment = ''
            try:
                linkToComment = "https://reddit.com/comments/" + post.link_id[3:] + "//" + post.id + "?context=10"
                print('[thread/answercomment] attempt to answer to comment: %s' %linkToComment)

                region = patternMatch.group('region')
                matchId = patternMatch.group('matchid')


                #do match analysis
                matchjson = match.requestMatch(matchId, region)
                response = drmatch.drMatch(matchjson)

                answerPost(post, response)

                return
            except:
                print('[thread/answercomment] reply to comment fail: %s' %linkToComment)

    patternsGame = ['acs\.leagueoflegends\.com/(?P<version>\w+)/stats/game/(?P<platformid>\w+)/(?P<matchid>\w+)\?gamehash=(?P<gamehash>\w+)',
                    'matchhistory\.(?P<region>\w+)\.leagueoflegends\.com/(?P<language>\w+)/#match-details/(?P<platformid>\w+)/(?P<matchid>\w+)\?gameHash=(?P<gamehash>\w+)']

    for pattern in patternsGame:
        patternGame = re.search(pattern, post.body, re.I)
        if patternGame != None:
            linkToComment = ''
            try:
                linkToComment = "https://reddit.com/comments/" + post.link_id[3:] + "//" + post.id + "?context=10"
                print('[thread/answercomment] attempt to answer to comment: %s' %linkToComment)

                gameHash = patternGame.group('gamehash')
                platformId = patternGame.group('platformid')
                matchId = patternGame.group('matchid')


                #do match analysis
                matchjson = game.requestGame(matchId, platformId, gameHash)
                response = drmatch.drMatch(matchjson)

                answerPost(post, response)

                return
            except:
                print('[thread/answercomment] reply to comment fail: %s' %linkToComment)



def answerPost(post, response):
    response = response + drouttro.ending


    i = 0
    while i < 20:
        i += 1
        try:
            answeredPost = post.reply(response)
            print('[thread/answerpost] successfully answered post')

            #TODO: add worker delete comments
            #addDeletionLinkToPost(answeredPost)

            break
        except:
            print('[thread/answerpost] answering to reddit post not successful, retrying in %s seconds' %(i*3))
            time.sleep(i*3)


def addDeletionLinkToPost(post):
    i = 0
    while i < 20:
        i += 1
        try:
            post.edit(post.body + drouttro.getDeletionLink(post))

            break
        except:
            print('[thread/answerpost] adding deletion link unsuccessful, retrying in %s seconds' %(i*3))
            time.sleep(i*3)
    print('[thread/answerpost] successfully added deletion link')