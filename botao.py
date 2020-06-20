import praw
import re
import time

reddit = praw.Reddit(client_id='v4WhY4bZgiJusw', client_secret='vT5rTvwdlLh49qV0_6VPl7Nd06c', user_agent="<console:redditbot:0.1 (by /u/bot_lulup)>",
username ='bot_lulup',
password='pedro123*')
reddit.validate_on_submit = True
subreddits = ['botesting', 'bottesting', 'testingground4bots']
pos = 0

title = "Testet"
url = "https://i.pinimg.com/564x/88/8e/a3/888ea32f3cddfc05a1aec2d68af5e8fd.jpg"

def post():
    global subreddits
    global pos

    subreddit = reddit.subreddit(subreddits[pos])
    subreddit.submit(title, url=url)

    pos = pos + 1

    if (pos >= len(subreddits) - 1):
        post()
    else:
        print ("Done")
post()