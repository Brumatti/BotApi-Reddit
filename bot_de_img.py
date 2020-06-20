import praw
import re
import time

reddit = praw.Reddit(client_id='v4WhY4bZgiJusw', 
client_secret='vT5rTvwdlLh49qV0_6VPl7Nd06c', 
user_agent="<console:redditbot:0.1 (by /u/bot_lulup)>",
username ='bot_lulup',
password='*******')

subreddits = ['testingground4bots', 'testabot']
pos = 0
errors = 0

title = "Teste"
url = "https://i.pinimg.com/564x/88/8e/a3/888ea32f3cddfc05a1aec2d68af5e8fd.jpg"

def post():
    global subreddits
    global pos
    global errors

    try:
        subreddits = reddit.subreddit(subreddits[pos])
        subreddits.submit(title, url=url)
        print("Posted to" + subreddits[pos])

        pos = pos + 1
        
        if (pos <= len(subreddits) - 1):
            post()
        else:
            print ("Feito")

    except praw.exceptions.APIException as e:
        if (e.error_type == "RATELIMIT"):
            delay = re.search("(\d+) minutes", e.message)
            if delay:
                delay_seconds = float(int(delay.group(1)) * 60)
                time.sleep(delay_seconds)
                post()
            else:
                delay = re.search("\d+) seconds", e.message)
                delay_seconds = float(delay.group(1))
                time.sleep(delay_seconds)
                post()
    except:
        errors = errors + 1
        if (errors > 5):
            print("crashou")
            exit(1)
post()
