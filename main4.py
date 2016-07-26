# coding=utf-8
import init
from converter import championconverter, itemconverter, spellconverter
from riotapi import matchlist, match
from displayreddit import drmatch

init.init()

#20267827 David
#2634415570 match

matchString = match.requestMatch(2634415570, 'euw')
drmatch.drMatch(matchString)

#print(matchlist.requestMatchList(20267827, 'euw'))
