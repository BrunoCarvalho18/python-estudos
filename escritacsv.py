with open('cadastro.csv','r') as arquivo:
    cadastro = arquivo.readlines()

    
cpf = input('CPF: ')
nome = input('Nome: ')
idade = input('Idade: ')
sexo = input('Sexo: ')
uf = input('UF: ')

registro = f'{cpf},{nome},{idade},{sexo},{uf}\n'

cadastro.append(registro)

with open('cadastro.csv','a') as arquivo:
    arquivo.writelines(registro)

    


