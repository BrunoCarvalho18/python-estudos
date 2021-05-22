def fahreinheit(T):
    return (9/5) * T + 32
def celsius(T):
    return (5/9) * T - 32

temp = [0,22.5,40,100]

#map é uma função que leva dois argumentos é o nome de uma função e a segunda é a sequencia
F_temps = list(map(fahreinheit,temp))

F_temps

list(map(celsius,F_temps))

list(map(lambda x: (5/9) *(x-32),F_temps))

