import  praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

subreddit_choice = input("Qual Subreddit deseja pesquisar?: ")
subreddit = reddit.subreddit(subreddit_choice)