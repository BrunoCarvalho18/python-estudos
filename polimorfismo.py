class Profissao:
    def __init__(self,classe= '',habilidade=''):
        self.classe= classe
        self.habilidade=habilidade

class Mago(Profissao):
    def __init__(self):
        self.classe='Mago'
        self.habilidade='Magia' 
    
    def atacar(self):
        return 'Ataque com Magia'

class Soldado(Profissao):
    
    def atacar(self):
        return 'Atacar de espada'

class Arqueiro(Profissao):
    
    def atacar(self):
        return 'ataque em distancia com arco e flecha'

m1 = Mago()
s1 = Soldado()
a1 = Arqueiro()
print(m1.atacar())
print(s1.atacar())
print(a1.atacar())