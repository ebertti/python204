import csv
arquivo = open('saida.csv', 'r', encoding='cp1252')
arq = csv.DictReader(arquivo)

for linha in arq:
    print(len(linha), linha)




