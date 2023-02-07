import re
import os

from flask import make_response
import requests
from bs4 import BeautifulSoup


def gerarSigla(expr:str):
    sigla = ''
    filtro = ('de', 'da', 'e')

    for termo in expr.strip().split(" "):
        if termo not in filtro:
            sigla += termo[0].upper() 
    
    print(sigla)
    return sigla


def onlycharacters(elemento:str, hint:str=""):
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if bool(re.search(r"\d", args[1])):
                raise ValueError(f"{elemento.capitalize()} não pode conter dígitos. " + hint)

            elif bool(re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(args[1])):
                raise ValueError(f"{elemento.capitalize()} não pode conter caracteres especiais. " + hint)

            return func(*args, **kwargs)
        return wrapper

    return decorator


def portalAlunoHTML():
    url = 'https://aluno.cefsa.edu.br/Login/Login'
    urlHome = 'https://aluno.cefsa.edu.br/Home'

    user = ''
    sec = ''

    values = {
        "Usuario":"",
        "Senha":""
    }

    with requests.Session() as ses:
        home = ses.post(url, data=values)
        # print(home, home.headers['Content-Type'], '\n')

        # print(home.text[:400])
        soup = BeautifulSoup(home.text, features="html.parser")

        text = './requests/arquivo.html'
        print(os.path.isfile(text))
        if not os.path.isfile(text):
            with open(text, "w") as html:
                html.write(soup.find('div', id="colapseCardapioSemanal").prettify())
                html.close()


def redirect_response(statuscode:int, route:str):
    response = make_response("", statuscode)
    response.headers["X-Redirect"] = route
    return response


def bad_request(statuscode:int, error_message:str):
    response = make_response("", statuscode)
    response.headers["Error-Message"] = error_message
    return response


def cursoID_select(aux, curso):

    curso_id = aux.dao.curso.get(
        aux.dao.query.nome == curso
    ).doc_id

    return curso_id