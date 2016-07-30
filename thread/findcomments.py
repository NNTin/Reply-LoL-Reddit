import time
import sqlite3
import thread
from reddit.redditconfig import SUBREDDIT, KEYWORDS, IGNOREAUTHORS, PRIVILEDGEDAUTHORS, MAXPOSTS, WAIT, CLEANCYCLES
#from thread import analyzecontent

def findComments(r):
    subreddit = r.get_subreddit(SUBREDDIT)

    cycles = 0

    sql = sqlite3.connect('scannedcomments.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS oldposts(id TEXT)')

    time.sleep(2)

    while True:
        try:
            print('[thread/findcomments] Searching %s' %SUBREDDIT)

            posts = list(subreddit.get_comments(limit=MAXPOSTS))
            posts.reverse()

            for post in posts:
                pid = post.id

                cur.execute('SELECT * FROM oldposts WHERE ID=?', [pid])
                if cur.fetchone():
                    #print('[thread/findcomments] already replied to comment')
                    continue

                try: pauthor = post.author.name
                except AttributeError:
                    print('[thread/findcomments] author is deleted, skipped')
                    continue

                if pauthor.lower() == r.user.name.lower():
                    #print('[thread/findcomments] will not reply to myself')
                    continue

                if IGNOREAUTHORS != [] and any(ignoreauthor.lower() == pauthor.lower() for ignoreauthor in IGNOREAUTHORS):
                    print['[thread/findcomments] Post made by ignore author, do not reply to: %s' %pauthor]
                    continue

                cur.execute('INSERT INTO oldposts VALUES(?)', [pid])
                sql.commit()


                pbody = post.body.lower()
                if any(key.lower() in pbody for key in KEYWORDS):
                    try:
                        linkToComment = "https://reddit.com/comments/" + post.link_id[3:] + "//" + post.id + "?context=10"
                        print('[thread/findcomments] starting analyzecontent thread on comment %s' %linkToComment)

                        #TODO: write analyze content thread
                    except:
                        print('@ [thread/findcomments] analyzecontent thread crashed!')
            cycles += 1

        except:
            print('[thread/findcomments] thread crashed, probably failed at get comments')

        if cycles >= CLEANCYCLES:
            print('[thread/findcomments] Cleaning database')
            cur.execute('DELETE FROM oldposts WHERE id NOT IN (SELECT id FROM oldposts ORDER BY id DESC LIMIT ?)', [MAXPOSTS * 2])
            sql.commit()
            cycles = 0
        print('[thread/findcomments] Running again in %d seconds' % WAIT)
        time.sleep(WAIT)