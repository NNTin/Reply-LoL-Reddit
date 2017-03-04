import time
import threading
from reddit import loginreddit
from reddit.redditconfig import SUBREDDIT, KEYWORDS, IGNOREAUTHORS, PRIVILEDGEDAUTHORS, MAXPOSTS, WAIT
from thread import answerpost

#def findComments(r):
def findComments():
    r = loginreddit.r

    subreddit = r.subreddit(SUBREDDIT)


    time.sleep(2)

    while True:
        try:
            print('[thread/findcomments] Searching %s' %SUBREDDIT)

            posts = subreddit.stream.comments()

            for post in posts:

                try: pauthor = post.author.name
                except AttributeError:
                    print('[thread/findcomments] author is deleted, skipped')
                    continue

                if pauthor.lower() == r.user.me():
                    #print('[thread/findcomments] will not reply to myself')
                    continue

                if IGNOREAUTHORS != [] and any(ignoreauthor.lower() == pauthor.lower() for ignoreauthor in IGNOREAUTHORS):
                    print['[thread/findcomments] Post made by ignore author, do not reply to: %s' %pauthor]
                    continue


                pbody = post.body.lower()
                if any(key.lower() in pbody for key in KEYWORDS):
                    try:
                        linkToComment = "https://reddit.com/comments/" + post.link_id[3:] + "//" + post.id + "?context=10"
                        print('[thread/findcomments] found post, analyzing post... %s' %linkToComment)

                        t = threading.Thread(target=answerpost.analyzePost, args = (post,))
                        t.start()

                        #TODO: write analyze content thread
                    except:
                        print('@ [thread/findcomments] answercomment thread crashed!')

        except:
            print('[thread/findcomments] thread crashed, probably failed at get comments')

        print('[thread/findcomments] Running again in %d seconds' % WAIT)
        time.sleep(WAIT)