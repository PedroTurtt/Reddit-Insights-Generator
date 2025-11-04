from reddit_scrapping import reddit_parameters
from json_manager import load_json
from llm_file import resumo_llm
import sys

# Aqui puxa a função do reddit_scrapping.py e gera o arquivo JSON
reddit_parameters()

# Função principal, onde vai puxar a função do arquivo llm_file.py
def main():
    print("Tentando carregar dados de 'dados_reddit.json'...")
    dados_carregados = load_json("dados_reddit.json")

    # Tratativa caso ocorra erros na leitura do arquivo
    if dados_carregados is None:
        print("ERRO FATAL: Falha ao carregar dados. Não é possível continuar.")
        sys.exit(1)

    if not isinstance(dados_carregados, (list, dict)) or not dados_carregados:
        print("AVISO: O arquivo 'dados_reddit.json' foi lido, mas está vazio ou em formato inesperado. Não é possível gerar o resumo.")
        print(f"Tipo de dados lidos: {type(dados_carregados)}")
        sys.exit(1)
        
    print(f"Dados carregados com sucesso. Total de posts: {len(dados_carregados)}")

    print("-" * 30)
    sucesso = resumo_llm(dados_carregados)

    if sucesso:
        print("\nProcesso concluído com sucesso!")
    else:
        print("\nProcesso concluído com falhas na geração do resumo.")


if __name__ == "__main__":
    main()