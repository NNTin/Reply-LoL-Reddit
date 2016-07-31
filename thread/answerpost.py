import re, time
from riotapi import match
from displayreddit import drmatch, drouttro
from reddit import loginreddit

sampleString = 'http://matchhistory.euw.leagueoflegends.com/en/#match-details/EUW1/2776212251/23337069? \n' \
               'http://www.lolking.net/summoner/euw/20267827#matches/2776212251 \n' \
               'http://www.lolskill.net/match/EUW/2776212251 \n' \
               'http://lolprofile.net/summoner/euw/RG%20Markal \n'

patternsMatchId = ['matchhistory\.(?P<region>\w+)\.leagueoflegends\.(?P<domain>\w+)/(?P<language>\w+)/#match-details/(?P<region2>\w+)/(?P<matchid>\w+)/(?P<playerid>\w+)', #leagueoflegends.com
            'lolking.net/summoner/(?P<region>\w+)/(?P<playerid>\w+)#matches/(?P<matchid>\w+)', #lolking.net
            'lolskill.net/match/(?P<region>\w+)/(?P<matchid>\w+)'] #lolskill.net

def analyzePost(post):
    #Checking for match id link
    for pattern in patternsMatchId:
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


def answerPost(post, response):
    response = response + drouttro.ending

    i = 0
    while i < 20:
        i += 1
        try:
            answeredPost = post.reply(response)
            print('[thread/answerpost] successfully answered post')

            addDeletionLinkToPost(answeredPost)

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