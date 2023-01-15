'''SchoolWebApp - Main Controller'''
from model.curso import Curso
from model.estudante import Estudante
from dao.cursoDAO import CursoDAO
from dao.estudanteDAO import EstudanteDAO
import utils.helper as functions

from flask import Flask, request, render_template as render
from flask import *  # render_template, redirect, url_for, make_response


app = Flask(__name__)


# @app.after_request
# def add_cache_header(response):
#     if request.path.startswith('/static/'):
#         # Set cache control to one year
#         response.cache_control.max_age = 31536000
#         response.expires = datetime.utcnow() + timedelta(seconds=3600)
#         return response


@app.route('/')
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

@app.route('/app-school/curso')
@app.route('/app-school/curso/listar')
def curso_listar():
    return render('/curso/listar.html', cursos=CursoDAO().listar())


@app.route('/app-school/curso/novo')
def curso_novo():
    return render('/curso/inserir.html')


# @app.route('/app-school/curso/gerar-sigla', methods = ['POST'])
# def curso_sigla():
#     nome_curso = request.field['nome']
#     return functions.gerarSigla(nome_curso), 200


@app.route('/app-school/curso/inserir', methods=['POST'])
def curso_inserir():

    try:
        curso = Curso(request.form['nome'], request.form['sigla'])
        CursoDAO().inserir(curso)
        return  make_response(url_for('curso_listar'), 200)

    except ValueError as e: 
        print(e.args[0])
        return  make_response(jsonify(status='error', message='param is missing'), 400)
        

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
    if request.method == 'POST':
        curso = Curso(request.form.get('nome'), request.form['sigla'])
        CursoDAO().remover(curso)
        return redirect(url_for('curso_listar'))


#######################################
#                                     #
# .:ESTUDANTE                         #
#                                     #
#######################################

@app.route('/app-school/estudante')
@app.route('/app-school/estudante/listar')
def estudante_listar():
    return render('/estudante/listar.html', estudantes=EstudanteDAO().listar())


@app.route('/app-school/estudante/novo')
def estudante_novo():
    return render('/estudante/inserir.html', cursos=CursoDAO().listar())


@app.route('/app-school/estudante/inserir', methods=['POST'])
def estudante_inserir():
    if request.method == 'POST':
        estudante = Estudante(
            request.form['nome'],
            request.form['matricula'],
            Curso(request.form['curso'], None))
        EstudanteDAO().inserir(estudante)
        return redirect(url_for('estudante_listar'))


@app.route('/app-school/estudante/alterar', methods=['GET'])
def estudante_alterar():
    estudante = Estudante(None, request.args.get('matricula'), None)
    return render('estudante/alterar.html',
                  estudante=EstudanteDAO().listarPorID(estudante),
                  cursos=CursoDAO().listar())


@app.route('/app-school/estudante/confirmar-alteracao', methods=['POST'])
def estudante_confirmar_alteracao():
    if request.method == 'POST':
        print(request.method)
        print(request.form.get('nome'))
        print(request.form.get('matricula'))
        estudante = Estudante(
            request.form.get('nome'),
            request.form.get('matricula'),
            Curso(request.form.get('curso'), None))
        EstudanteDAO().alterar(estudante, request.form.get('matricula'))
        return redirect(url_for('estudante_listar'))


@app.route('/app-school/estudante/remover')
def estudante_remover():
    estudante = Estudante(None, request.args.get('matricula'), None)
    return render('/estudante/remover.html',
                  estudante=EstudanteDAO().listarPorID(estudante),
                  cursos=CursoDAO().listar())


@app.route('/app-school/estudante/confirmar-exclusao', methods=['POST'])
def estudante_confirmar_exclusao():
    if request.method == 'POST':
        estudante = Estudante(
            None,
            request.form.get('matricula'),
            None
        )
        EstudanteDAO().remover(estudante)
        return redirect(url_for('estudante_listar'))

#######################################
#                                     #
# .:ENDEREÇOS                         #
#                                     #
#######################################