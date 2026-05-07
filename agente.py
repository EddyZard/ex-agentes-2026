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

    