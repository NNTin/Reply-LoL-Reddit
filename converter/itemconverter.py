from riotapi.item import itemDictionary

itemConverter = {}

def updateItemConverter():
    global itemConverter

    template = '[](#i-{name})'
    for itemId in itemDictionary:
        itemConverter[itemId] = template.format(name=itemDictionary[itemId].replace(' ', '').replace("'", '').replace(':','').lower().replace('-','').replace('(','').replace(')','').replace('.',''))
