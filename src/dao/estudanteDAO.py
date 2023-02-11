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


    def inserir(self, estudante:Estudante):
        self.dao.estudante.insert({
            'nome': estudante.nome,
            'matricula': estudante.matricula,
            'curso': estudante.curso.codigo
        })


    def alterar(self, estudante:Estudante, query:str):
        self.dao.estudante.update({
            'nome': estudante.nome,
            'matricula': estudante.matricula,
            'curso': estudante.curso.codigo
            }, cond=(self.dao.query.matricula == query)
        )


    def remover(self, estudante:Estudante):
        self.dao.estudante.remove(
            self.dao.query.matricula == estudante.matricula
        )


    def listar(self):
        
        query = []
        for estudante in self.dao.estudante.all():
            query.append(
                Estudante(
                    estudante['nome'],
                    estudante['matricula'],
                    CursoDAO().buscarPorID(estudante['curso'])
                )
            )

        return query
            


    def buscarPorID(self, id:str):
        result = self.dao.estudante.get(
            self.dao.query.matricula == id.strip()
        )
        
        return Estudante(
            result.get('nome'), 
            result.get('matricula'),
            CursoDAO().buscarPorID(result.get('curso'))
        )