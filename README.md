# 🤖 Reddit Insights Generator

## Visão Geral

O **Reddit Insights Generator** é uma ferramenta Python que realiza o scraping de posts e comentários de um subreddit específico, armazena esses dados em um arquivo JSON e, em seguida, utiliza o modelo de Linguagem Grande (LLM) **Gemini 2.5 Flash** para gerar um resumo conciso e informativo sobre o tema, sentimento e principais pontos de discussão encontrados.

## ✨ Funcionalidades

  * **Scraping Dinâmico do Reddit:** Coleta posts, comentários e respostas de qualquer subreddit e termo de busca definidos pelo usuário (via PRAW).
  * **Filtros de Busca:** Permite ordenar os resultados por Relevância, Destaque, Mais Votados ou Mais Novos.
  * **Gerenciamento de Dados:** Salva e carrega os dados brutos em formato JSON (`dados_reddit.json`).
  * **Análise e Resumo LLM:** Utiliza a API do Google Gemini para processar o JSON e criar um resumo de alto nível com título, visão geral, top 3 insights e conclusão de sentimento.

## 🛠️ Instalação e Configuração

### Pré-requisitos

Você precisará ter o Python instalado (versão 3.10+ recomendada).

### 1\. Clonar o Repositório

```bash
git clone <https://github.com/PedroTurtt/Reddit-Insights-Generator.git>
cd reddit-insights-generator
```

### 2\. Instalar Dependências

O projeto utiliza as bibliotecas `praw`, `google-genai` e `python-dotenv`.

```bash
pip install praw google-genai python-dotenv
```

### 3\. Configurar Variáveis de Ambiente

Crie um arquivo chamado **`.env`** na raiz do projeto para armazenar suas chaves de API e credenciais do Reddit.

#### Chaves de API

Você precisará de:

1.  **Chave da API Gemini:** Obtenha no [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).
2.  **Credenciais do Reddit:** Crie um aplicativo [aqui](https://www.reddit.com/prefs/apps/) para obter `client_id` e `client_secret`.
      * *Nota:* As credenciais `REDDIT_USERNAME` e `REDDIT_PASSWORD` são usadas para autenticação com o PRAW, além disso, não utilize autentificação de 2 fatores.

O arquivo `.env` deve se parecer com este:

```env
# Chave da API do Google Gemini
GEMINI_API_KEY="SUA_CHAVE_GEMINI_AQUI"

# Credenciais do Reddit (PRAW)
REDDIT_CLIENT_ID="SEU_CLIENT_ID_AQUI"
REDDIT_CLIENT_SECRET="SEU_CLIENT_SECRET_AQUI"
REDDIT_USER_AGENT="SeuUserAgentPersonalizadoAqui" # Ex: RedditScraperV1.0
REDDIT_USERNAME="SEU_USERNAME_AQUI"
REDDIT_PASSWORD="SUA_PASSWORD_AQUI"
```

## 🚀 Como Executar

Execute o script principal diretamente:

```bash
python main.py
```

O programa irá guiar você com prompts interativos:

1.  **Digite o nome do Subreddit desejado:** (Ex: `investimentos`)
2.  **O que deseja procurar?:** (Ex: `bitcoin`)
3.  **Quantidade de posts para salvar:** (Ex: `10`)
4.  **Filtrar por:** Escolha a ordenação (1 a 4).

Após a coleta dos dados, o script irá:

1.  Salvar os dados brutos em `dados_reddit.json`.
2.  Chamar a API Gemini para analisar o JSON.
3.  Salvar o resumo gerado em **`resumo.txt`**.

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada. Orquestra a coleta de dados e a geração do resumo. |
| `reddit_scrapping.py` | Contém a lógica de scraping usando PRAW e a coleta de posts/comentários. |
| `json_manager.py` | Funções utilitárias para salvar (`save_json`) e carregar (`load_json`) arquivos JSON. |
| `llm_file.py` | Lógica para se conectar à API Gemini e gerar o resumo com base no prompt. |
| `.env` | Arquivo para armazenar as credenciais e chaves de API de forma segura. |
| `dados_reddit.json` | Arquivo gerado com os dados brutos coletados do Reddit. |
| `resumo.txt` | Arquivo gerado com a análise e resumo do LLM. |
