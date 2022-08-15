import praw
import random
import time

reddit = praw.Reddit(client_id='v4WhY4bZgiJusw', 
client_secret='vT5rTvwdlLh49qV0_6VPl7Nd06c', 
user_agent="<console:reddit_bot:0.1>",
username ='bot_lulup',
password='INSIRA SUA SENHA'
)

subreddit = reddit.subreddit("testabot")

palavras_tristes = ["Triste época! É mais fácil desintegrar um átomo do que um preconceito. Albert Einstein",
"A vida não é triste. Tem horas tristes. Romain Rolland",
"A amizade duplica as alegrias e divide as tristezas. Francis Bacon",
"Maior que a tristeza de não haver vencido é a vergonha de não ter lutado!. Rui Barbosa ",
"Se algumas pessoas se afastarem de você, não fique triste, isso é resposta da oração: “livrai-me de todo mal, amém”. Caio Fernando Abreu",
"Não há nada melhor para uma alma do que tornar menos triste outra alma. Paul Verlaine"]

for post in subreddit.hot(limit=10):
    #print("********")
    #print(post.title)

    for comment in post.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("------")
                print(comment.body)
                #-1 pra dar um número entre 0 e 5 e não 0 e 6
                random_index = random.randint(0, len(palavras_tristes) - 1)
                comment.reply(palavras_tristes[random_index])
                time.sleep(660)
