# Dados imutaveis

tuplas = (0,1,2,3,4)
tuplas +=4,5,6,7
string = ''
inteiros = 1
floats = 10.5

def soma(num1,num2,res):
    res = num1 + num2
    return res

#a = 0
#b = 70
#c Vai acontecer um erro
#d nenhuma das anteriores

#Dados mutáveis

lists = [0,1,2,3,"jujuba"]
dic = {}
dic['nova_chave'] = 1

def adiciona_item(lista,item):
    lista.append(item)

adiciona_item(lists, 'macarrão')
