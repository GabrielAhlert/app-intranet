from django.shortcuts import render
import requests
from decouple import config
from django.http import HttpResponseRedirect, HttpResponse as Http

def get_cotacao(request):
    try:
        headers = { 'Authorization' : 'Bearer ' + config('COTRISOJA_API_TOKEN'), 'Content-Type': 'application/json'}
        url = 'https://sp-app.cotrisoja.com.br/api/'
        url_cotacao = url + requests.get(url + 'dashboard', headers=headers).json()['agricultural_quotation']['formats']['large']['url']
        return HttpResponseRedirect(url_cotacao)
    except:
        return Http('Erro ao buscar cotação')
