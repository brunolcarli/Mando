"""
Módulo dedicado a definição de algoritmos para requisições à APIs externas.
"""
from ast import literal_eval
from sys import stdout
import requests
from gql import gql


class Queries:
    """
    Consultas graphql
    """

    @staticmethod
    def get_quotes(server):
        """
        Solicita os quotes de um servidor.
        """
        query = f'''
        query {{
            botQuotes(server: "{server}")
        }}
        '''
        return gql(query)


class Mutations:
    """
    Operações graphql de criação e alteração de dados.
    """

    @staticmethod
    def create_quote(message, server):
        """
        Solicita a criação de uma mensagem para um servidor.
        """
        mutation = f'''
        mutation {{
            botCreateQuote(input:{{
                quote:"{message}"
                server: "{server}"
            }}){{
                response
            }}
        }}
        '''
        return gql(mutation)


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
