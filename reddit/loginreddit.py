import praw, obot

r = 0

def loginReddit():
    global r
    r = praw.Reddit(client_id=obot.client_id,
                    client_secret=obot.client_secret,
                    user_agent=obot.user_agent,
                    username=obot.username,
                    password=obot.password)
