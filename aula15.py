import copy
# copy - retorna uma cópia rasa (shallow copy)


pessoa = {
    'Nome': 'Lucas Samuel',
    'Sobrenome': 'Figueiredo',
    'Idade': 20,
    'lista': [0, 1, 2],
}

dicionario2 = pessoa.copy() #metodo copy faz com que o "dicionario2" não afete o "pessoa".
#método copy só copia dados imutáveis. Dados mutáveis como listas e tuplas não são copiados e sim linkados
#Ou seja, um dicionário irá apontar para o item do outro dicionário (Quando alterar algo na lista de um, irá alterar nas duas listas).

dicionario2 = copy.deepcopy(pessoa) #Para que não se tenha problemas ao copiar os dicionários que possuem
#listas, é recomendado que utilize o "copy.deepcopy()" após importar o "Copy" no inicio do código

dicionario2['Nome'] = 'Maria'
dicionario2 = ['lista'][1] = 9999
print(pessoa)
print(dicionario2)