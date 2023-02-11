from utils.helper import *
from model.curso import Curso


class Estudante:
    def __init__(self, nome:str, matricula:str, curso:Curso):  # codigo
        # self.codigo = codigo
        self.nome = nome
        self._matricula = matricula.strip()
        self.curso = curso


    # def __repr__(self) -> str:
        # return f"<Curso(name={self.nome!r})>"


    def __call__(self) -> None:
        print(self._matricula)
        print(self.nome)
        print('---')
        print(self.curso.nome)


    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    @onlycharacters('nome')
    def nome(self, n: str):
        self._nome = n.strip()

    @property
    def matricula(self) -> str:
        return self._matricula

    @property
    def curso(self) -> Curso:
        return self._curso

    @curso.setter
    def curso(self, c:Curso):
        self._curso = c