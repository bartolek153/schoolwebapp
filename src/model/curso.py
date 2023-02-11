from utils.helper import *


class Curso:
    def __init__(self, nome= "", sigla="", codigo:int=None):
        self.nome = nome
        self.sigla = sigla
        self._codigo = codigo


    # def __repr__(self) -> str:
    #     return f"<Curso(name={self.nome!r})>"


    def __call__(self) -> None:
        print(self._codigo)
        print(self.nome)
        print(self.sigla)


    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    @onlycharacters('nome')
    def nome(self, n: str):
        self._nome = n.strip()

    @property
    def sigla(self) -> str:
        return self._sigla

    @sigla.setter
    @onlycharacters('sigla', 'Utilize o gerador embutido.')
    def sigla(self, s: str):
        self._sigla = s.strip()

    @property
    def codigo(self) -> str:
        return self._codigo