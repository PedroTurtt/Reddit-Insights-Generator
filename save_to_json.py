import json

def save_json(filename, info):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)
        print("Arquivo gerado com sucesso!")

    except Exception as e:
        print(f"Erro ao gerar Json: {e}")

def load_json(file_name_to_load):
    try:
        with open(file_name_to_load, "r", encoding="utf-8") as f:
            dados = json.load(f)
            print(f"Dados carregados com sucesso!")
    except FileNotFoundError:
        print(f"Erro, arquivo não foi encontrado")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None