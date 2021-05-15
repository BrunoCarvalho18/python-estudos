dic ={
    'nome': 'Bruno Carvalho',
    'idade': 32,
    'dados': [0,1,2,3,4],
    'tupla': [0,1,2,3]
}

print(dic['tupla'])
print(dic['tupla'][2])

for chave in dic.keys():
    if chave == 'idade':
        print(f'achei - ',dic[chave])

for valor in dic.values():
    if valor == '32':
        print('achei a idade')

for chave, valor in dic.items():
   print(f'key:{chave} - value: {valor}')

a,b,c = 1,2,3
print(f'a=> {a} - b => {b} - c = {c}') # a=>1, b=>2. c=>3
