import  praw
import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("REDDIT_USER_AGENT"))

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT"),
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD")
)

subreddit_choice = input("Qual Subreddit deseja pesquisar?: ")
subreddit = reddit.subreddit(subreddit_choice)

busca = input("O que deseja procurar?: ")

for submission in subreddit.search(busca, sort="new", limit=3):
    print(f"ID: {submission.id}")
    print(f"Título: {submission.title}")
    print(f"Autor: {submission.author}")
    print(submission.selftext)
    for comment in submission.comments:
        print(f"Comentário: {comment.body}")
        for reply in comment.replies:
            print(f"   ↳ Resposta: {reply.body}")
    print("-" * 40)


