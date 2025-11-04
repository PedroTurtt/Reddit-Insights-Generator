import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
import json

load_dotenv()

# Conecta na API do Gemini 
try:
    client = genai.Client ()
except Exception as e:
    print("Erro ao inicializar o cliente Gemini. Verifique a chave GEMINI_API_KEY no seu .env.")
    print(f"Detalhes: {e}")
    exit()

# Função que pega arquivo JSON, pega o prompt e gera o resumo em arquivo .txt
def resumo_llm(dados_json, arquivo_saida="resumo.txt"):
    dados_string = json.dumps(dados_json, indent=2, ensure_ascii=False)

    prompt = f"""
    Você é um assistente de análise de dados. Sua tarefa é analisar o seguinte conjunto 
    de dados do Reddit em formato JSON, que contém posts e seus comentários/respostas, e 
    fornecer um resumo conciso e informativo sobre o tema principal, o sentimento geral 
    e os pontos de discussão mais relevantes.

    **O Resumo deve conter:**
    1. Título do Resumo.
    2. Uma visão geral do que foi encontrado (o tema e o contexto).
    3. Os 3 principais pontos de discussão ou insights extraídos dos posts e comentários.
    4. Uma conclusão sobre o sentimento geral da comunidade (positivo, negativo ou neutro/misto).

    **Dados do Reddit (JSON):**
    ---
    {dados_string}
    ---
    """

    print("Gerando resumo com modelo LLM")

    # Configuração do modelo e qual prompt usar
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        resumo = response.text
        
        # Abertura do arquivo JSON
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(resumo)
            
        print(f"[LLM] Resumo gerado e salvo em **{arquivo_saida}** com sucesso!")
        return True

    # Caso ocorra erros relacionados a API ou geração de resumo, aqui vai gerar o motivo
    except APIError as e:
        print(f"Erro na API do Gemini: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado durante a geração do resumo: {e}")
        return False    