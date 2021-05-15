import json

with open('dados.json','r') as json_file:
     dados = json.load(json_file)

print(dados)
print('\n')
print('Nome:' + dados['nome'])
print('Insta:' + dados['instagram'])
print('Linguagem:' + dados['linguagem'])
