"""SchoolWebApp - Main Controller"""
import sys
import os

from model.curso import Curso
from model.estudante import Estudante
from dao.cursoDAO import CursoDAO
from dao.estudanteDAO import EstudanteDAO
import utils.helper as functions
import utils.constants as constantes

from flask import Flask, request, render_template as render
from flask import *  # render_template, redirect, url_for, make_response


# Starting the app

app = Flask(__name__)


# Application Middleware

# @app.after_request
# def default_headers(response):
#     pass


# Routes

@app.route("/")
@app.route("/app-school")
@app.route("/app-school/")
@app.route("/app-school/index")
@app.route("/app-school/index.html")
def index():
    return render("index.html")


#######################################
#                                     #
# .:CURSO                             #
#                                     #
#######################################


@app.route("/app-school/curso")
@app.route("/app-school/curso/listar")
def curso_listar():
    return render("/curso/listar.html", cursos=CursoDAO().listar())


@app.route("/app-school/curso/novo")
def curso_novo():
    return render("/curso/inserir.html")


@app.route("/app-school/curso/gerar-sigla", methods=["POST"])
def curso_sigla():
    nome = request.get_json()
    return jsonify(functions.gerarSigla(nome)), 200


@app.route("/app-school/curso/inserir", methods=["POST"])
def curso_inserir():
    try:
        curso = Curso(request.form["nome"], request.form["sigla"])
        CursoDAO().inserir(curso)
        return functions.redirect_response(201, constantes.main_routes["curso"])

    except ValueError as e:
        return functions.bad_request(422, e.args[0])


@app.route("/app-school/curso/alterar", methods=["GET"])
def curso_alterar():
    codigo = request.args.get("codigo")
    return render("curso/alterar.html", curso=CursoDAO().buscarPorID(codigo))


@app.route("/app-school/curso/confirmar-alteracao", methods=["POST"])
def curso_confirmar_alteracao():
    try:
        curso = Curso(request.form.get("nome"), request.form.get("sigla"))
        CursoDAO().alterar(curso, request.form.get("query"))
        return functions.redirect_response(201, constantes.main_routes["curso"])
        
    except ValueError as e:
        return functions.bad_request(422, e.args[0])


@app.route("/app-school/curso/remover", methods=["GET"])
def curso_remover():
    codigo = request.args.get("codigo")
    return render("curso/remover.html", curso=CursoDAO().buscarPorID(codigo))


@app.route("/app-school/curso/confirmar-exclusao", methods=["POST"])
def curso_confirmar_exclusao():
    try:
        curso = Curso(request.form.get("nome"), request.form.get("sigla"), request.form.get("query"))
        CursoDAO().remover(curso)
        return functions.redirect_response(201, constantes.main_routes["curso"])

    except Exception as e:
        return functions.bad_request(422, e.args[0])


#######################################
#                                     #
# .:ESTUDANTE                         #
#                                     #
#######################################


@app.route("/app-school/estudante")
@app.route("/app-school/estudante/listar")
def estudante_listar():
    return render("/estudante/listar.html", estudantes=EstudanteDAO().listar())


@app.route("/app-school/estudante/novo")
def estudante_novo():
    return render("/estudante/inserir.html", cursos=CursoDAO().listar())


@app.route("/app-school/estudante/inserir", methods=["POST"])
def estudante_inserir():
    try:
        id = functions.cursoID_select(CursoDAO(), request.form["curso"])

        estudante = Estudante(
            request.form["nome"],
            request.form["matricula"],
            CursoDAO().buscarPorID(id)
        )
        EstudanteDAO().inserir(estudante)
        return functions.redirect_response(201, constantes.main_routes["estudante"])

    except ValueError as e:
        return functions.bad_request(422, e.args[0])


@app.route("/app-school/estudante/alterar", methods=["GET"])
def estudante_alterar():
    matricula = request.args.get("matricula")
    return render(
        "estudante/alterar.html",
        estudante=EstudanteDAO().buscarPorID(matricula),
        cursos=CursoDAO().listar()
    )


@app.route("/app-school/estudante/confirmar-alteracao", methods=["POST"])
def estudante_confirmar_alteracao():
    try:   
        id = functions.cursoID_select(CursoDAO(), request.form.get("curso"))
        matricula = request.form.get("matricula")

        estudante = Estudante(
            request.form.get("nome"),
            matricula,
            CursoDAO().buscarPorID(id)
        )
        EstudanteDAO().alterar(estudante, matricula)
        return functions.redirect_response(201, constantes.main_routes["estudante"])

    except Exception as e:
        return functions.bad_request(422, e.args[0])


@app.route("/app-school/estudante/remover")
def estudante_remover():
    matricula = request.args.get("matricula")
    return render(
        "/estudante/remover.html",
        estudante=EstudanteDAO().buscarPorID(matricula),
        cursos=CursoDAO().listar()
    )


@app.route("/app-school/estudante/confirmar-exclusao", methods=["POST"])
def estudante_confirmar_exclusao():
    try:
        estudante = Estudante(
            request.form.get("nome"),
            request.form.get("matricula"),
            None
        )
        EstudanteDAO().remover(estudante)
        return functions.redirect_response(201, constantes.main_routes["estudante"])

    except Exception as e:
        return functions.bad_request(422, e.args[0])


# EstudanteDAO().inserir(
#     Estudante(
#         "lbart asdf", 
#         "5563",
#         CursoDAO().buscarPorID(1)
#     )
# )


if __name__ == "__main__":
   app.run(host="0.0.0.0", port="5000", debug=True)