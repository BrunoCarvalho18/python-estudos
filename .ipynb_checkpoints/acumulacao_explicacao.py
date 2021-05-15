

#lista de compras
lista_de_compras = [
    ('Camiseta',19.90),
    ('Calça Jeans',20.50),
    ('Meia G',5.90)
]

indice = 0
total_de_compras = 0    

while indice < len(lista_de_compras):
    total_de_compras += lista_de_compras[indice][1]
    indice +=1

print(f'O total de compras do seu carrinho: {total_de_compras}')

print('resolução com for')