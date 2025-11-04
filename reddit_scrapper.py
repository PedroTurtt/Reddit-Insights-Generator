import  praw
import os
from dotenv import load_dotenv
from save_to_json import save_json

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT"),
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD")
)

subreddit = reddit.subreddit("maconha_legal") #reddit.subreddit(subreddit_choice)
busca = "associação" #input("O que deseja procurar?: ")
limit_number = input('Quantidade de posts que deseja buscar: ')

collected_info = []
print('Iniciando a busca: ')


for submission in subreddit.search(busca, sort="relevance", limit=3):

    post_info = {
        "id": submission.id,
        "titulo": submission.title,
        "autor": str(submission.author),
        "texto_post": submission.selftext,
        "comentarios": []
    }

    print(f"coletando post: {submission.title}")

    submission.comments.replace_more(limit=0)
  
    for comment in submission.comments.list():
        comnetario_info = {
            "autor": str(comment.author),
            "comentario": comment.body,
            "respostas": []
        }
        for reply in comment.replies:
            resposta_info = {
            "autor": str(reply.author),
            "texto": reply.body
            }
            comnetario_info["respostas"].append(resposta_info)

        post_info["comentarios"].append(comnetario_info)

    collected_info.append(post_info)

save_json("dados_reddit.json", collected_info)