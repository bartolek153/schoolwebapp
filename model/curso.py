class Curso:

    def __init__(self, codigo, nome, sigla):
        self.codigo = codigo
        self.nome = nome
        self.sigla = sigla

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getSigla(self):
        return self.sigla

    def setSigla(self, sigla):
        self.sigla = sigla
