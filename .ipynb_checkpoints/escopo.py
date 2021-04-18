#escopo de uma variavel:
#porção do código onde essa variável é reconhecida
#ou seja, local onde ela existe

def funcao():
    global x
    x = 42
    print("Conheco essa variavel?",x, a)

x = 1
a = 2
funcao()
print(x) 
