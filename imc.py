#1 Capturar informações de peso e altura
peso = float(input('Digite o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    printf(f'Baixo peso - IMC: {imc}')
elif imc < 24.9:
    print(f'Peso normal - IMC: {imc}')
elif imc < 29.9:
    print(f'Pré Obesidade - IMC: {imc}')
elif imc < 34.9:
    print(f'Obesidade Grau I - IMC: {imc}')
elif imc < 39.9:
    print(f'Obesidade Grau II - IMC: {imc}')
else:
    print(f'Obesidade Grau III - IMC: {imc}')