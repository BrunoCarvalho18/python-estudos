segundos =  int ( input ( " Insira uma quantidade de segundos: " ))
minutos = segundos // 60
segundos = segundos % 60
horas = minutos // 60

print(f"{horas}:{minutos}:{segundos}")