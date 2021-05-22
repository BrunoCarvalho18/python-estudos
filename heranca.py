class Mae:
    def __init__(self):
        self.nome = ''
        self.nacionalidade='Francesa'
    
    def falarFrances(self):
        return 'Bonjour!'

class Pai:
    def __init__(self):
        self.nome= ''
        self.nacionalidade='Inglesa'
    
    def falarIngles(self):
        return 'Good Afternoon!'
    
    def falarFrances(self):
        return 'Oui!'

class Filha(Mae,Pai):
    def falarFrances(self):
        return 'Oui'