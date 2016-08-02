# coding=utf-8
import init
import threading
from reddit import loginreddit
from thread.findposts import findComments

if __name__ == "__main__":
    print('[main] logging into reddit')
    loginreddit.loginReddit()

    print('[main] initialize dictionaries and converters (champion, item, spell)')
    init.init()
    r = loginreddit.r
    print('[main] starting findcomments thread')
    t = threading.Thread(target=findComments, args = ())
    t.start()


