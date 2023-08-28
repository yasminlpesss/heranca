class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        calculo = (self.nota1 + self.nota2) / 2
        print(calculo)


Media = Aluno('nome', 10, 6)
Media.calcular_media()