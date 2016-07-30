import praw, OAuth2Util
from reddit.redditconfig import APP_UA

r = 0

def loginReddit():
    global r
    r = praw.Reddit(APP_UA)
    o = OAuth2Util.OAuth2Util(r)
    o.refresh(force=True)
