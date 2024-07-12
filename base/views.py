from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect, HttpResponse as Http
from django.http import HttpResponseBadRequest
from decouple import config
import os
from requests.exceptions import RequestException as HttpRequestError
import json

def refresh_token():
    headers = { 'Content-Type': 'application/json'}
    url = config("COTACAO_URL")
    body = { {"email": config("COTACAO_USER"), "password": config("COTACAO_PASS")}}
    token = requests.post(url + 'admin/login', data=json.dumps(body), headers=headers).json()['data']['token']
    os.environ["COTRISOJA_API_TOKEN"] = token
    
def getToken():
    token = os.environ.get("COTRISOJA_API_TOKEN")
    if token:
        return token
    return "InvalidTokenRefresh"

def get_cotacao(request):
    try:
        headers = { 'Authorization' : 'Bearer ' +  getToken(), 'Content-Type': 'application/json'}
        url = 'https://sp-app.cotrisoja.com.br/api/'
        url_cotacao = url + requests.get(url + 'dashboard', headers=headers).json()['agricultural_quotation']['formats']['large']['url']
        return HttpResponseRedirect(url_cotacao)
    except:
        try:
            refresh_token()
            return get_cotacao(request)
        except:
            return HttpResponseBadRequest('Erro ao buscar cotação')
            pass
    
    
