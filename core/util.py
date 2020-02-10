"""
Módulo dedicado a ferramentas utilitárias
"""
import base64
from gql import Client
from gql.transport.requests import RequestsHTTPTransport


def get_gql_client(url, auth=None):
    """
    Retorna um client de execução de requisições graphql.
    param : auth : <str> : hash de autorização.
    """
    if not auth:
        transport = RequestsHTTPTransport(url=url, use_json=True)
    else:
        headers = {
            'content-type': 'application/json',
            'auth': '{}'.format(auth)
        }
        transport = RequestsHTTPTransport(
            url=url,
            use_json=True,
            headers=headers
    )

    client = Client(transport=transport, fetch_schema_from_transport=False)
    return client


def make_hash(descriptor, _id):
    """
    Criptografa um descritor e um id em uma hash base64

    args:
        descriptor : <str>
        id: <int> || <str>

    return: <str>
    """
    return base64.b64encode(b'%s' % f'{descriptor}:{_id}'.encode('utf-8'))
