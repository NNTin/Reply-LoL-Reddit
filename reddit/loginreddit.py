import praw, OAuth2Util
from reddit.redditconfig import APP_UA

def loginReddit():
    r = praw.Reddit(APP_UA)
    o = OAuth2Util.OAuth2Util(r)
    o.refresh(force=True)