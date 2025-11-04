import json

# Função responsavel pela criação do JSON
def save_json(filename, info):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)
        print("Arquivo gerado com sucesso!")

    except Exception as e:
        print(f"Erro ao gerar Json: {e}")

# Função responsavel pela leitura do JSON
def load_json(file_name_to_load):
    try:
        with open(file_name_to_load, "r", encoding="utf-8") as f:
            dados = json.load(f)
            print(f"Dados carregados com sucesso!")
            return dados
    except FileNotFoundError:
        print(f"Erro, arquivo não foi encontrado")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None