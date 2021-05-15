#Parte 1 
## definições de funções auxiliares, constantes

opcoes={
    '1':lambda x,y: x +y,
    '2':lambda x,y: x-y,
    '3':lambda x,y: x*y,
    '4':lambda x,y: x/y,
    '5':lambda x,y: exit()
}

def menu():
 while True:
    # Capturar dois números:
    n1 = float(input('n1: '))
    n2 = float(input('n2: '))

# Apresentar opções para o usuário
    print(f'Digite a opção desejada:\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5-sair')

# Solicitar ao usuário a opção desejada
    op = input('')

# Realizar a operação de acordo com a escolha do usuário
    if op in opcoes.keys():
        print(opcoes[op](n1,n2))
    else:
      print('Opção inválida')

if __name__ == '__main__':
    menu()

