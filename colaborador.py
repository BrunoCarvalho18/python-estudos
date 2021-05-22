class Colaborador:
    def __init__(self):
        self.nome = ''
        self.endereco= ''
        self.idade = 0
        self.salario = 0
        self.cargo = ''
        self.encargos = 0.25 
    
    def apresentaColaborador(self):
        return f'Colaborador: {self.nome}\n'\
               f'Cargo : {self.cargo}\n'\
               f'Salario:{self.salario:.2f}\n'

class Gerente(Colaborador):
    def calculaSalario(self,bonus):
        return self.salario * bonus
    
g1 = Gerente()
g1.salario = 1500

print(g1.calculaSalario(1.5))
