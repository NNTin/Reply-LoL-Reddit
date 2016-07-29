SUBREDDIT = "ReplyLoLReddit"
#SUBREDDIT = "AnalyzeLast100Games+Dota2+LearnDota2"
# This is the sub or list of subs to scan for new posts. For a single sub, use "sub1". For multiple subreddits, use "sub1+sub2+sub3+..."
KEYWORDS = ["matches/", "players/"]
# These are the words you are looking for
IGNOREAUTHORS = []
# Ignore these authors fdsfjkl
PRIVILEDGEDAUTHORS = ['lumbdi']
# These authors can force the bot to delete his own comments
MAXPOSTS = 100
# This is how many posts you want to retrieve all at once. PRAW can download 100 at a time.
WAIT = 10
# This is how many seconds you will wait between cycles. The bot is completely inactive during this time.
CLEANCYCLES = 10
# After this many cycles, the bot will clean its database
# Keeping only the latest (2*MAXPOSTS) items

APP_UA = 'LoL responder made by /u/lumbdi'              #user agent (please change yours)
BOTNAME = 'Reply-LoL-Reddit'
