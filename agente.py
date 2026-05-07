import requests   # Biblioteca para fazer requisições HTTP

# Variáveis imutáveis
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"   # http://locahost/
MODEL = "qwen2.5:0.5b"                               # Modelo de texto leve


def agente_buscador(tema):
    url = "https://pt.wikipedia.org/w/api.php"

 #Dict com parametos da api da Wikipedia
    parametros = {
        'action' : 'query',  
        'list' : 'search',
        'srsearch' : tema,   # Qual é a String de Busca
        'format' : 'json',   # Formato de resposta que será retornado
        'utf8' : 1,          # Se eu quero ou não usar a codificação UTF8 (1 = sim, 0 = não)
        'srlimit' : 5        # O limite de tópicos na busca
    }

    headers = {
        'User-Agent' : 'AgenteAula/1.0 (269565@unifio.edu.br)'  # Identificação para "credencial" de entrada
    }

# Padrão para consultar uma API:
    resposta = requests.get( 
        url,
        params= parametros,
        headers = headers,
        timeout=10           # Tempo que espera a resposta, se não for estabelecido, ele apenas usa o Timeout Padrão (ele espera "pra sempre", por volta de 1 ou 2 minutos [porém é o python que irá encerrar a request e não a biblioteca em si])
    )

    resposta.raise_for_status()   # Se for um código de resposta normal (20X), caso contrário ele para a aplicação

        # Tratamento de dados
    dados = resposta.json()

    resultados = []

    for item in dados['query']['search']:
        trecho = item['snippet']

        trecho = trecho.replace(
            '<span class="searchmatch">',
            ""
        )

        trecho = trecho.replace(
            "</span>",
            ""
        )

        resultados.append({
            'titulo' : item['title'],
            'trecho' : trecho,
            'link' : f"https://pt.wikipedia.org.wiki/{item['title'].replace(' ', '_')}"
        })

    return resultados

# Testando o Agente
# print(agente_buscador('Copa do Mundo de Futebol')) 


def chamar_ollama(prompt):
    resposta = requests.post(
        OLLAMA_URL,
        json={
            'model' : MODEL,
            'prompt' : prompt,
            'stream' : False
        },
        timeout=120
    )

    resposta.raise_for_status()

    dados = resposta.json()

    return dados['response']


teste = """
Aja como um especialista me Ciência da Computação

Tarefa:
Defina vetores em estruturas de dados
"""

print(chamar_ollama(teste))