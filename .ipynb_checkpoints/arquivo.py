# Leitura de um arquivo

arquivo = open('arquivo.txt','r')

conteudo = arquivo.readlines()

arquivo.close()

print(conteudo)