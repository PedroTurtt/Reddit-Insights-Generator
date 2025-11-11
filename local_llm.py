import ollama
import time
import json

# O modelo já deve ter sido baixado (como no Passo 2)
MODELO_PARA_USAR = 'gemma3:4b'

def gerar_resposta(dados_json, arquivo_saida="resumo.txt"):
    print(f"Iniciando chat com o modelo: {MODELO_PARA_USAR}")

    dados_string = json.dumps(dados_json, indent=2, ensure_ascii=False)

    try:
        start_time = time.time()
        
        # Esta é a chamada "no código"
        response = ollama.chat(
            model=MODELO_PARA_USAR,
            messages=[
                {'role': 'user', 'content': f"{dados_string} Você é um assistente de análise de dados. Sua tarefa é analisar o seguinte conjunto de dados do Reddit em formato JSON, que contém posts e seus comentários/respostas, e fornecer um resumo conciso e informativo sobre o tema principal, o sentimento geral e os pontos de discussão mais relevantes em português. **O Resumo deve conter:**1. Título do Resumo.2. Uma visão geral do que foi encontrado (o tema e o contexto).3. Os 3 principais pontos de discussão ou insights extraídos dos posts e comentários.4. Uma conclusão sobre o sentimento geral da comunidade (positivo, negativo ou neutro/misto)."},
            ]
        )
        
        end_time = time.time()
        
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(response['message']['content'])
        print(f"[Local LLM] Resumo gerado e salvo em **{arquivo_saida}** com sucesso!")
        print(f"\nTempo de resposta: {end_time - start_time:.2f} segundos")
        return True

    except Exception as e:
        print(f"Erro: Não foi possível conectar ao Ollama.")
        print("Verifique se o aplicativo Ollama está em execução no seu PC.")