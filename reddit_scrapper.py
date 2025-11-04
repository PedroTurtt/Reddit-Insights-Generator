import praw
import os
from dotenv import load_dotenv
from json_manager import save_json

def case_match(value):
    match value:
        case 1:
            return "relevance" 
        case 2:
            return "hot"
        case 3:
            return "top"
        case 4:
            return "new"
        case _:
            return "new"

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent=os.environ.get("REDDIT_USER_AGENT"),
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD")
)
def reddit_parameters():
    subreddit_choice = input("Digite o nome do Subreddit desejado: ")
    subreddit = reddit.subreddit(subreddit_choice)
    busca = input("O que deseja procurar?: ")
    limit_number = int(input("Quantidade de posts para salvar: "))
    
    print(f"1-Relevance|2-Hot|3-Top|4-New")
    value = input()
    try:
        value_int = int(value)
    except ValueError:
        print(f"Entrada inválida '{value}'. Usando a opção padrão.")
        value = 1

    search = case_match(value)
    print("pesquisa escolhida: ",search)

    print('subreddit escolhido: ',subreddit)
    print('termo para busca: ',busca)

    collected_info = []
    print('Iniciando a busca: ')


    for submission in subreddit.search(busca, sort=search, limit=limit_number):

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