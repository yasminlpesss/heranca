class retangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base


    def calcular_area(self):
        calculo = self.base * self.altura
        print(calculo)



Quadrilatero = retangulo(4, 6)
Quadrilatero.calcular_area()

