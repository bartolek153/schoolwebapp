from tinydb import TinyDB, Query
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# Data Access Object:
# Camada de acesso ao banco de dados,
# restringida a modificacoes apenas dentro da classe (private)


class DAO(object):

    # Convencao Python: um atributo, cujo identificador apresente a
    # sequencia '__' de caracteres no inicio, traz a ideia de
    # modificador de acesso private
    __instancia = None

    # Metodo estatico, ou seja, nao pertence a um objeto, e sim,
    # a classe. Logo, nao precisa instanciar a classe para utiliza-lo
    def getInstancia():
        if DAO.__instancia is None:
            DAO()
        return DAO.__instancia

    def __init__(self):
        self.db = TinyDB(os.path.join(parentdir, 'database', 'db.json'))

        self.curso = self.db.table('Curso')
        self.estudante = self.db.table('Estudante')

        self.query = Query()

        # Verifica se a instancia e unica
        if DAO.__instancia is not None:
            raise Exception('Essa classe é um singleton, logo, ',
                            'só pode existir um único objeto')
        else:
            DAO.__instancia = self

    def inserir(self):
        pass

    def alterar(self):
        pass

    def remover(self):
        pass

    def listar(self):
        pass

    def listarPorIDS(self):
        pass
