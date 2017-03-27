from reddit import loginreddit


ending = '---\n' \
         '[^^source](https://github.com/NNTin/Reply-LoL-Reddit) ^^on ^^github, ' \
         '[^^hover](#a "Reply-LoL-Reddit isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.") ^^for ^^disclosure, ' \
         '[^^message](https://www.reddit.com/message/compose/?to=lumbdi) ^^the ^^owner ^^on [^^Discord](https://discord.gg/Dkg79tc)'

def getDeletionLink(post):
    r = loginreddit.r
    botName = r.user.name

    endingSuffixTemplate = '^^, [^^click]({url} "Only works for bot summoner and /r/leagueoflegends mods! Do not change already filled out form!") to delete'
    deletionLinkTemplate = 'https://www.reddit.com/message/compose/?to=' + botName + '&subject=deletion&message={fullname}'

    deletionLink = deletionLinkTemplate.format(fullname=post.fullname)
    endingSuffix = endingSuffixTemplate.format(url=deletionLink)

    return endingSuffix