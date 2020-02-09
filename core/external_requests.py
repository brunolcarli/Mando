"""
Módulo dedicado a definição de algoritmos para requisições à APIs externas.
"""
from ast import literal_eval
from sys import stdout
import requests

def get_random_meme():
    """
    Realiza uma requisição à API de memes aleatórios.
    Retorna uma tupla contendo o status da requisição e os dados.
    Os dados são um dicionário contendo a resposta da requisição.
    Os dado somente são retornados em caso de status 200, do contrário um
    dicionário vazio.
        - return <tuple> : (int, dict)
    """
    response = requests.get('http://meme-api.herokuapp.com/gimme')
    try:
        data = literal_eval(response.text)
    except Exception as ex:
        stdout.write(str(ex))
        data = dict()

    return response.status_code, data
