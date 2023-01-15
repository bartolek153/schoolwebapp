# https://docs.pylonsproject.org/projects/colander/en/latest/basics.html
# https://dev.to/murtuzaalisurti/dark-mode-toggle-animation-using-css-27il
# https://speckyboy.com/css-javascript-snippets-dark-light-mode/
# https://simpleweblearning.com/how-to-create-light-dark-mode-toggle-with-css-and-javascript/
# https://stackoverflow.com/questions/60037491/how-to-save-cookies-for-dark-light-mode-toggle
# https://replit.com/talk/templates/Dark-and-Light-Modes-with-Flask/128745 ver /static/main.css
# https://pythonbasics.org/what-is-flask-python/
# https://flask.palletsprojects.com/en/2.2.x/deploying/
# https://github.com/mikeroyal/Self-Hosting-Guide
# https://www.geeksforgeeks.org/flask-rendering-templates/
# https://learn.microsoft.com/pt-br/visualstudio/python/learn-flask-visual-studio-step-03-serve-static-files-add-pages?view=vs-2022#step-3-4-use-template-inheritance-to-create-a-header-and-nav-bar


import os

import requests
from bs4 import BeautifulSoup
from requests_oauth2client import OAuth2ClientCredentialsAuth

def enderecoAPIv1(cep):
    #cep = cep.trim.removeSpaces().replace('-','')
    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get(url)
    print(response, resp.url)
    print(response.text)

    return response

def enderecoAPIv2(cep):

    #When you send your first request, OAuth2ClientCredentialsAuth will automatically retrieve an access token from the AS using the Client Credentials grant, then will include it in the request. Next requests will use the same token, as long as it is valid. A new token will be automatically retrieved once the previous one is expired
    url = f'https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/60130240{cep}'
    TokenJWT = 'https://h-apigateway.conectagov.estaleiro.serpro.gov.br/oauth2/jwt-token'

    auth = OAuth2ClientCredentialsAuth(
        oauth2client, scope="", resource="https://myapi.local"
    )
    
    response = requests.get(url, auth=auth)
    print(response)

enderecoAPIv2('09070340')

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