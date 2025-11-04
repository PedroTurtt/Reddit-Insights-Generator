import json

def save_json(filename, info):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)
        print("Arquivo gerado com sucesso!")

    except Exception as e:
        print(f"Erro ao gerar Json: {e}")