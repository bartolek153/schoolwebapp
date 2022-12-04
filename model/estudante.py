class Estudante(object):
    def __init__(self, nome: str, matricula: str, curso):  # codigo
        # self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    # def getCodigo(self):
    #     return self.codigo
    #
    # def setCodigo(self, codigo):
    #     self.codigo = codigo

    def getMatricula(self) -> str:
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getNome(self) -> str:
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso
