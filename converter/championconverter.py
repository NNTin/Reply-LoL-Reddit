from riotapi.champion import championDictionaryById

championConverter = {}

def updateChampionConverter():
    global championConverter

    template = '[](#c-{name})'
    for championId in championDictionaryById:
        championConverter[championId] = template.format(name=championDictionaryById[championId].lower())
