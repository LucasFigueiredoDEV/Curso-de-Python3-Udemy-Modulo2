# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Lucas Samuel'
pessoa['sobrenome'] = 'Figueiredo'


print(pessoa[chave])

pessoa[chave] = 'Luiza'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None: # Avalia se sobrenome existe na lista, 
    #importante utilizar "is None", pois  retorna none por valor padrão caso não exista.
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')