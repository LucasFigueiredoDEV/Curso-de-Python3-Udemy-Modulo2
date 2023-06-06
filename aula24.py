# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.


# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) #.sort ordena a lista #O reverse = True serve para mudar a ordem, ou seja, do menor para o maior ou maior para o menor.
# sorted(lista)#serve para ordenar a lista também, com a diferença na forma de escrever o código

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista.sort(key=lambda item: item ['nome']) #Uma função em uma única linha

for item in lista:
    print(item)