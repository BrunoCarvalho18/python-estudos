class Pilha:
    def __init__(self):
        self.pilha = []
        self.topo = 0
        
    def empilhar(self,item):
        self.pilha.append(item)
        self.topo +=1
    
    def desempilhar(self):
       if not self.estaVazia():
        item_removido = self.pilha[-1]
        del self.pilha[-1]
        self.topo -= 1
        return f'o item {item_removido} foi retirado da pilha'
      return 'Pilha está vazia'
    
    def estaVazia(self):
        return len(self.pilha) == 0
        
p = Pilha()
p.empilhar(1)