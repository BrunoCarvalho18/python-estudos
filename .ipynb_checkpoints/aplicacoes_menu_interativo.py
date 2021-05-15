
while True:
    op = input('Digite a opção desejada:\n1- Saudação\n2- Sair\n3- Nenhuma das Alternativas')

    if op == '1':
        print('uma saudação qualquer')
    elif op == '2':
        break
    elif op == '3':
        continue
    else:
        print('Opção inválida')
print('fim')