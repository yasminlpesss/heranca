class conta:
    def __int__(self,titular,saldo,numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
    def depositar(self,deposito):
        self.saldo +=depositar
    def sacar(self,saque):
        self.saldo-=saque
    def exibir(self):
        print(f'o saldo atual e:', {self.saldo})


conta1= conta("bruno",1000,3567)
a = int(input('digite o valor'))
conta1.sacar(a)
conta.exibir()
b=int(input('digite o valor'))
conta1.depositar(b)
conta.exibir


