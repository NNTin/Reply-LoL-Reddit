from reddit import loginreddit


ending = '---\n' \
         '[^^source](https://github.com/NNTin/Reply-LoL-Reddit) ^^on ^^github, ^^testing'

def getDeletionLink(post):
    r = loginreddit.r
    botName = r.user.name

    endingSuffixTemplate = ', [^^deletion ^^link]({url} "Only works for bot summoner and /r/leagueoflegends mods! Do not change already filled out form!")'
    deletionLinkTemplate = 'https://www.reddit.com/message/compose/?to=' + botName + '&subject=deletion&message={fullname}'

    deletionLink = deletionLinkTemplate.format(fullname=post.fullname)
    endingSuffix = endingSuffixTemplate.format(url=deletionLink)

    return endingSuffix