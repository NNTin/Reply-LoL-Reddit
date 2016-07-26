from riotapi.spell import spellDictionaryById

spellConverter = {}

def updateSpellConverter():
    global spellConverter

    template = '[](#ss-{name})'
    for spellId in spellDictionaryById:
        spellConverter[spellId] = template.format(name=spellDictionaryById[spellId].lower())