class Cachorro:
    def __init__(self,nome,idade,latir):
        self.nome = nome
        self.idade = idade
        self.latir = latir


    def latir(self):
        print('whoolf!')

caracteristicas = Cachorro('andy','5 anos',True)
Cachorro = caracteristicas

Cachorro.nome()