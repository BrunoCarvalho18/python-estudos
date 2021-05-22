## Arquivos em formato TXT/CSV

with open('cadastro.csv','r') as arquivo:
    cadastro = arquivo.readlines()

filtro_uf = 'RJ'

for registro in cadastro:
    if filtro_uf in registro.split(',')[4]:
        print('CPF:', registro.split(',')[0])
        print('Nome:', registro.split(',')[1])
        print('Idade:', registro.split(',')[2])
        print('UF:', registro.split(',')[3])
              