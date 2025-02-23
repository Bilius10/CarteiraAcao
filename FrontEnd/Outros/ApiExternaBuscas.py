import requests
import matplotlib.pyplot as plt
import pandas as pd
from Outros.session import session

def nomeAcoes():
    
    try:
        
        response = requests.get("http://localhost:8080/external/API/nomes")
        
        if(response.status_code == 200):
            
            data = response.json()
        
            return data.get("stocks", [])
        else:
            return []

    except requests.exceptions.RequestException as e:
        return {"Erro": "Nenhuma ação encontrada", "Detalhes": str(e)}  

def infoAcoes(nomeAcao):

    try:

        response = requests.get("http://localhost:8080/external/API/"+nomeAcao)

        if(response.status_code == 200):
            return response
        else:
            return {
                    "results": [
                        {
                            "longName": "null",
                            "regularMarketDayHigh": 0.0,
                            "regularMarketDayLow": 0.0,
                            "logourl": "null",
                            "regularMarketVolume": 0
                        }
                    ]
                    }
        
    except requests.exceptions.RetryError as e:
        return str(e)
    
def InfoAcoes30diasEditada():
    headers = {"Authorization": "Bearer "+session.user_data.get('token')}
    response = requests.get("http://localhost:8080/acao/infoAcao/"+str(session.user_data.get('idLogin')), headers=headers)
    data = response.json()

    return data

def InfoAcoes30diasCompleta(acao):
    response = requests.get("http://localhost:8080/external/API/30dias/"+acao)
    data = response.json()

    return data

def acoesUsuario():
    headers = {"Authorization": "Bearer "+session.user_data.get('token')}
    response = requests.get("http://localhost:8080/acao/usuario/"+str(session.user_data.get('idLogin')), headers=headers)
    data = response.json()

    return data

def CadastrarAcaoNaCarteira(parametros):
    headers = {"Authorization": "Bearer "+session.user_data.get('token')}

    response = requests.post("http://localhost:8080/acao/save", json=parametros, headers=headers)
    
    return response