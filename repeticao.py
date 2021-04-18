#evitar repeticao de codigo

vegetais = ['abacate','cenoura','maçã']

for i in range(len(vegetais)):
    #iteracao
    print("primeira lista: ",vegetais[i])

for vegetal in vegetais:
    print("segunda lista: ",vegetal)

# for variavel in iterável/conjunto

for letra in 'Bruno':
    print(letra)