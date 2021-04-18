import csv

with open('arquivo.csv',newline='') as csvfile:
    lerlinha = csv.reader(csvfile,delimiter= ' ',quotechar='|')
    for linha in lerlinha:
        print(','.join(linha))