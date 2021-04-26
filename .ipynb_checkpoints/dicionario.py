#dicionarios

traducoes = {
    'gato':'cat',
    'cachorro':'dog',
    'mesa': 'table'

}

numeros = {'one':1, 'two':2, 'three':3}

print(traducoes)
print(numeros)


#conjunto de chaves/valor
for chave in traducoes.keys():
    print(chave,"->",traducoes[chave])

# - cada chave é única
for palavra in traducoes.values():
    print(palavra)