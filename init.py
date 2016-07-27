from riotapi import champion, item, match, matchlist, spell, summoner
from converter import championconverter, itemconverter, gameconstants, spellconverter

def init():
    initializeDictionaries()
    initializeConverters()

def initializeDictionaries():
    champion.updateChampionDictionary()
    item.updateItemDictionary()
    spell.updateSpellDictionary()

def initializeConverters():
    championconverter.updateChampionConverter()
    itemconverter.updateItemConverter()
    spellconverter.updateSpellConverter()
