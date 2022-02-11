import requests, os
from time import time
import json
import pandas as pd
import io

BASE_URL = "https://neuromancer.4kst.com"

KEY_ID = ""
KEY_SECRET = ""

def send_request(request_list, auth):
    """
    Descrição:
        Função para fazer o login na 4KST e preparar o modelo
        para consumo. Ao realizar o login, e recebido um token
        para realizar os requests.
    Parâmetros:
        request_list (list(dict)): Lista de dicionários contendo as instâncias
                                para serem enviadas para a API.
        auth        (string): Token de autenticação.
    Output:
        Lista de dicionários contendo id e probs.
    """
    url = f"{BASE_URL}/consult"
    json_header = {'Authorization': auth, 'Accept': 'application/json', 'Content-Type': 'application/json'}
    payload = str(request_list).replace('\'', '"')

    response = requests.request("POST", url, headers=json_header, data = payload)
    if response.status_code != 200:
        print("Error!")
        print(response)
    else:
        response = response.text
    response = response.replace('true', 'True')
    response = response.replace('false', 'False')
    response = eval(response)

    return response['message']

def set_online(auth):
    """
    Descrição:
        Função para levantar o modelo 4KST. É importante levantar
        antes para não acabar perdendo requisições por timeout.
    Parâmetros:
        auth        (string): Token de autenticação.
    """

    url = f"{BASE_URL}/appService/setOnline"

    payload = {}
    headers = {
      'Authorization': auth
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    if response.text == 'OK':
        return True
    else:
        print(response.text)
    return False

def is_online(auth):
    """
    Descrição:
        Função para checar se o modelo está disponível.
    Parâmetros:
        auth        (string): Token de autenticação.
    """
    url = f"{BASE_URL}/appService/isOnline"

    payload = {}
    headers = {
    'Authorization': auth
    }

    response = requests.request("GET", url, headers=headers, data = payload).text
    response = response.replace('true', 'True')
    response = response.replace('false', 'False')
    response = eval(response)
    return response['isOnline']

def score_file_model(auth, df):
    """
    Descrição:
        Função para atualizar o modelo.
    Parâmetros:
        auth        (string): Token de autenticação.
        df          (pd.DataFrame): Dados de atualização.
    """
    df.to_csv('.tempfile', index=False, encoding='utf-8-sig')


    url = f"{BASE_URL}/consult/"

    payload = {}
    files = [('.tempfile', open('.tempfile','rb'))]
    headers = {
        'Connection': 'keep-alive',
        'Authorization': auth,
    }
    response = requests.request("POST", url, headers=headers, data = payload, files = files)
    if response.status_code == 200:
        response = json.loads(response.text)
    else:
        os.remove('.tempfile')
        raise Exception("Could not get the watcher code properly. Reason: \n" + str(response.text))
    return response['request_watcher_id']


def download_arquivo(auth, watcher_id, scorename="SCORE"):
    url = f"{BASE_URL}/consult/file/{watcher_id}"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Authorization': f'{auth}'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    df_scores = pd.read_csv(io.StringIO(response.content.decode('utf-8')), sep=',')
    df_scores[scorename] = (df_scores['prob_1'] * 1000).astype(int)
    df_scores['id'] = df_scores['id'].astype(str)
    df_scores = df_scores[['id', scorename]]
    return df_scores


def watcher_request(auth, watcher_id):
    """
    Descrição:
        Função para observar um processo.
    Parâmetros:
        auth        (string): Token de autenticação.
        watcher_id  (string): ID do processo.
    """
    url = f"{BASE_URL}/watcher/{watcher_id}"

    payload = {}
    headers = {
      'Authorization': auth
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    response = json.loads(response.text)
    return response['request_watcher_status_id']


class Authenticator:
    def __init__(self):
        self._generate_token()

        # Tempo de expiração em minutos.
        self.expiration_time = 15

    def _login(self):
        """
        Descrição:
            Ao realizar o login, e recebido um token para realizar os requests.
        Output:
            Token de sessão.
        """
        url = f"{BASE_URL}/auth/login/key"

        payload = {}
        headers = {
            'Authorization': f'{KEY_ID}:{KEY_SECRET}'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        token = eval(response.text)['token']
        return token

    def _generate_token(self):
        """
        Descrição:
            Registrar um novo token e realizar o controle de tempo de login.
        """
        self.token = self._login()
        self.token_time = time()

    def get(self):
        """
        Descrição:
            Controla o tempo e retorna o token.
        Output:
            Token de acesso.
        """
        if (time() - self.token_time)/60 > self.expiration_time:
            self._generate_token()
        return self.token
