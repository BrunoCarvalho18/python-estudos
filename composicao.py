class Produto:
    def __init__(self,
            sku = '',
            nome = '',
            desc = '',
            preco = 0.0
    ):
        
    self.sku = sku
    self.nome = nome
    self.desc = desc
    self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.carrinho = []
        self.quantidade_produtos = 0
        self.total = 0
    
    def adiconarProduto(self,produto):
        self.carrinho.append(produto)
        self.quantidade_produtos +=1
        
    def removerProduto(self,nome_produto):
        removido = False
        
        for produto in self.carrinho and not removido:
            if produto.nome == nome_produto:
                self.carrinho.remove(produto)
                removido = True
                return f'O produto {nome_produto} não foi encontrado'
    
    def calculaTotal(self):
        soma = 0
        for produto in self.carrinho:
            soma += produto.preco
        
        return soma