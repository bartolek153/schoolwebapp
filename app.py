'''Main App Controller'''

from model.curso import Curso
# from model.estudante import Estudante
from dao.cursoDAO import CursoDAO
# from dao.estudanteDAO import EstudanteDAO

# set FLASK_APP=app.py && flask run
from flask import Flask, render_template as render, request, redirect, url_for
# from flask import * ?

app = Flask(__name__)


@app.route('/')
def runing():
    return "<h5>running</h5>"


@app.route('/app-school')
@app.route('/app-school/')
@app.route('/app-school/index')
@app.route('/app-school/index.html')
def index():
    return render('index.html')


#######################################
#                                     #
# .:CURSO                             #
#                                     #
#######################################

@app.route('/app-school/curso/listar')
def curso_listar():
    return render('/curso/listar.html', cursos=CursoDAO().listar())


@app.route('/app-school/curso/novo')
def curso_novo():
    return render('/curso/inserir.html')


@app.route('/app-school/curso/inserir', methods=['POST'])
def curso_inserir():
    curso = Curso(request.form['nome'], request.form['sigla'])
    CursoDAO().inserir(curso)
    return redirect(url_for('curso_listar'))

##
# verificao para saber se curso ja foi cadastrado
##


@app.route('/app-school/curso/alterar', methods=['GET'])
def curso_alterar():
    curso = Curso(request.args.get('nome'), None)
    return render('curso/alterar.html', curso=CursoDAO().listarPorID(curso))


@app.route('/app-school/curso/confirmar-alteracao', methods=['POST'])
def curso_confirmar_alteracao():
    if request.method == 'POST':
        curso = Curso(request.form.get('nome'), request.form.get('sigla'))
        CursoDAO().alterar(curso, request.form.get('query'))
    return redirect(url_for('curso_listar'))


@app.route('/app-school/curso/remover', methods=['GET'])
def curso_remover():
    curso = Curso(request.args.get('nome'), None)
    return render('/curso/remover.html', curso=CursoDAO().listarPorID(curso))


@app.route('/app-school/curso/confirmar-exclusao', methods=['POST'])
def curso_confirmar_exclusao():
    curso = Curso(request.form.get('nome'), request.form['sigla'])
    CursoDAO().remover(curso)
    return redirect(url_for('curso_listar'))


#######################################
#                                     #
# .:ESTUDANTE                         #
#                                     #
#######################################
# , estudantes=EstudanteDAO().listar())
@app.route('/app-school/estudante/listar')
def estudante_listar():
    return render('/estudante/listar.html')
