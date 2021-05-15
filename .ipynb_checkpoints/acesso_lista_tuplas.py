lista = [0,1,2,3, ('11-11-2020',88.50),[5,6,7,8]]

print(lista[0])
print(lista[-1])

matriz =[
    [0,1,2],
    [3,4,5],
    [6,7,8],
]

print('tamnaho de linhas matriz:', len(matriz))

soma = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
         soma += matriz[linha][coluna]

print(soma)
