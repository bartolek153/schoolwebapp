class Estudante(object):
    def __init__(self, codigo, nome, matricula, curso):
        self.codigo = codigo
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso
