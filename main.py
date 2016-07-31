# coding=utf-8
import init
import threading
from reddit import loginreddit
from thread.findposts import findComments
from thread import answerpost

if __name__ == "__main__":
    print('[main] logging into reddit')
    loginreddit.loginReddit()

    print('[main] initialize dictionaries and converters (champion, item, spell)')
    init.init()
    r = loginreddit.r
    print('[main] starting findcomments thread')
    t = threading.Thread(target=findComments, args = ())
    t.start()

	#answercomment.analyzeComment()





    #20267827 David
    #2634415570 match 2770739260

    #matchString = match.requestMatch(2770739260, 'euw')
    #print(drmatch.drMatch(matchString) + drouttro.getOuttro())

    #champion.updateChampionDictionary()
    #championconverter.updateChampionConverter()
    #dict = championconverter.championConverter


