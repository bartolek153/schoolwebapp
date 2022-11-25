from model.curso import Curso
from model.estudante import Estudante
from dao.cursoDAO import CursoDAO


cursoDAO = CursoDAO()

adm = Curso(1, "Administração", "ADM")
ea = Curso(2, "Engenharia de Alimentos", "EA")
eca = Curso(3, "Engenharia de Controle e Automação", "ECA")
ec = Curso(4, "Engenharia de Computação", "EC")

cursoDAO.inserir(adm)
cursoDAO.inserir(ea)
cursoDAO.inserir(eca)
cursoDAO.inserir(ec)


for curso in cursoDAO.listar():
    print(curso.get('nome'), curso.get('sigla'))


print(adm.getCodigo(), adm.getNome(), adm.getSigla())
print(ea.getCodigo(), ea.getNome(), adm.getSigla())
print(eca.getCodigo(), eca.getNome(), eca.getSigla())
print(ec.getCodigo(), ec.getNome(), ec.getSigla())


alunoA = Estudante(1, "Luiza", "081220001", ea)
alunoB = Estudante(2, "Luiz", "081220002", eca)

print()
print("Estudantes:")
print("\tCodigo: ", alunoA.getCodigo())
print("\tMatricula: ", alunoA.getMatricula())
print("\tNome: ", alunoA.getNome())
print("\tCurso: ", alunoA.getCurso().getCodigo(),
      '-', alunoA.getCurso().getNome())

print()
print("\tCodigo: ", alunoB.getCodigo())
print("\tMatricula: ", alunoB.getMatricula())
print("\tNome: ", alunoB.getNome())
print("\tCurso: ", alunoB.getCurso().getCodigo(),
      '-', alunoB.getCurso().getNome())
