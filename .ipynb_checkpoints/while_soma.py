num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

while True:
    operacao = input('Digite a operação desejada:\n1- Mais\n2- Menos\n3- Dividir\n4- Mult\n')

    if operacao=='Mais':
        print('O resultado da soma é:',num1+num2)
    elif operacao=='Menos':
        print('O resultado da subtração é:',num1-num2)
    elif operacao=='Dividir':
        print('O resultado da divisão é:',num1/num2)
    elif operacao=='Mult':
        print('O resultado da multiplicação é:',num1*num2)
    else:
        print('Operação Inválida')
        break
print('Fim')
