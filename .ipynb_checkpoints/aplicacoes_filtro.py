texto = """

o rato roeu a roupa o rei de Roma

"""

vogal = 0

for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal+=1

print('total de vogais: {}'.format(vogal))


exit()

lista_de_compras =[
    ('Camiseta',19.90),
    ('Calça Jeans',20.50),
    ('Meia G',5.90)
]

total = 0
desconto = 0.9

for compra in lista_de_compras:
    total+=compra[1]

for compra in lista_compras:
    if 'camiseta' in compra[0].lower():
        total += compra[1] * desconto
    else:
        total += compra[1]

print(f'Valor total de compras aplicando o desconto: {total:.2f}')