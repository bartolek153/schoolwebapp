from model.curso import Curso
from model.estudante import Estudante
from dao.DAO import DAO
from dao.cursoDAO import CursoDAO

# set FLASK_APP=app.py && flask run
from flask import Flask, render_template as render, request

app = Flask(__name__)


@app.route('/')
def runing():
    return "<h5>running</h5>"


@app.route('/app-school')
def index():
    return render('index.html')


#######################################
#                                     #
# .:Curso                             #
#                                     #
#######################################

@app.route('/app-school/curso/listar')
def curso_listar():
    return render('/curso/listar.html')


@app.route('/app-school/curso/novo')
def curso_novo():
    return render('/curso/inserir.html')


@app.route('/app-school/curso/inserir', methods=['GET', 'POST'])
def curso_inserir():
    nome = request.form['nome']
    sigla = request.form['sigla']

    curso = Curso(1, nome, sigla)
    CursoDAO().inserir(curso)
    return "deu bom"


#######################################
#                                     #
# .:Estudante                         #
#                                     #
#######################################

@app.route('/app-school/estudante/listar')
def estudante_listar():
    return render('/estudante/listar.html')
