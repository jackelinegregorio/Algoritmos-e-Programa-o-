class aluno:
  def __init__(self, matricula, nome):
    self.matricula=matricula
    self.nome=nome
  def matricular(self):
    print("Aluno(a): ", self.nome, " matriculado(a)")

Jackeline = aluno("173678", "Jackeline Gregório")
print(Jackeline.matricula)
print(Jackeline.nome)
Jackeline.matricular()