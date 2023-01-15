from .cursoDAO import CursoDAO
from .DAO import DAO
from model.curso import Curso
from model.estudante import Estudante

import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class EstudanteDAO(DAO):

    def __init__(self):
        self.dao = DAO.getInstancia()

    def inserir(self, estudante: Estudante):
        self.dao.estudante.insert({
            'nome': estudante.getNome(),
            'matricula': estudante.getMatricula(),
            'curso': estudante.getCurso().getNome()
        })

    def alterar(self, estudante: Estudante, query: str):
        self.dao.estudante.update({
            'nome': estudante.getNome(),
            'matricula': estudante.getMatricula(),
            'curso': estudante.getCurso().getNome()},
            self.dao.query.matricula == query
        )

    def remover(self, estudante: Estudante):
        self.dao.estudante.remove(
            self.dao.query.matricula == estudante.getMatricula()
        )

    def listar(self):
        estudantes = []
        result = self.dao.estudante.all()
        for estudante in result:
            estudantes.append(
                Estudante(
                    estudante.get('nome'),
                    estudante.get('matricula'),
                    CursoDAO().listarPorID(
                        Curso(estudante.get('curso'), None)
                    )
                )
            )
        return estudantes

    def listarPorID(self, estudante: Estudante):
        result = self.dao.estudante.search(
            self.dao.query.matricula == estudante.getMatricula().strip())
        return Estudante(result[0].get('nome'), result[0].get('matricula'),
                         CursoDAO().listarPorID(
                             Curso(result[0].get('curso'), None)))
