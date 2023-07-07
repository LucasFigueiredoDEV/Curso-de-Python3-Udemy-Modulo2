# groupby - agrupando valores (itertools)
from itertools import groupby


alunos = [
    {'Nome': 'Lucas', 'Nota': 'A'},
    {'Nome': 'Letícia', 'Nota': 'B'},
    {'Nome': 'Beatriz', 'Nota':'A'},
    {'Nome': 'Luana', 'Nota': 'C'},
    {'Nome': 'João', 'Nota': 'D'},
    {'Nome': 'Eduardo', 'Nota': 'A'}
]

letras = ['a', 'a', 'a', 'a', 'b', 'c', 'a']

#grupos = groupby(sorted(letras)) #É preciso ordenar utilizando sorted para que ele não acabe criando um outro grupo, por estar em ordem diferente

#for chave, grupo in grupos:
#    print(chave)
#    print(list(grupo))


alunos_agrupados = sorted(alunos, key=lambda a: a['Nota'])

grupos = groupby(alunos_agrupados, key=lambda a: a['Nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)