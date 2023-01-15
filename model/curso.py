import re

class Curso:
    def __init__(self, nome:str, sigla:str, codigo:int=None):
        self.nome = nome
        self.sigla = sigla
        self._codigo = codigo
    
    def __repr__(self) -> str:
        return f"<Curso(name={self.nome!r})>"

    def __call__(self) -> None:
        print(self.codigo)
        print(self.nome)
        print(self.sigla)

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, n:str):
        if (bool(re.search(r'\d', n))):
            raise ValueError("Um nome não pode conter dígitos.")

        self._nome = n

    @property
    def sigla(self) -> str:
        return self._sigla

    @sigla.setter
    def sigla(self, s:str):
        self._sigla = s

    @property
    def codigo(self) -> str:
        return self._codigo