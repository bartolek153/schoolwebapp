from .DAO import DAO
from model.curso import Curso

import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class CursoDAO(DAO):

    def __init__(self):
        self.dao = DAO.getInstancia()


    def inserir(self, curso:Curso):
        self.dao.curso.insert({
            'nome': curso.nome, 
            'sigla': curso.sigla,
        })


    def alterar(self, curso:Curso, id:int):
        self.dao.curso.update({
            'nome': curso.nome, 
            'sigla': curso.sigla
            }, doc_ids=[int(id)]
        )


    def remover(self, curso:Curso):
        self.dao.curso.remove(
            None, doc_ids=[int(curso.codigo)]
        )


    def listar(self):
        return self.dao.curso.all()


    def buscarPorID(self, id:int):
        result = self.dao.curso.get(None, id)
        return Curso(result.get('nome'), result.get('sigla'), result.doc_id)