import json


#pessoa = {
#    'Nome': 'Lucas',
#    'Sobrenome': 'Figueiredo',
#    'Enderecos': [
#        {'Rua': 'r1', 'numero': 88},
#        {'Rua': 'r2', 'numero': 77},
#    ],
#    'Altura': 1.75,
#    'Numeros_preferidos': (1, 2, 3, 7, 10),
#    'dev': True,
#    'nada': None,
#}

#with open('aula59.json', 'w', encoding='utf-8') as arquivo:
#    json.dump(
#        pessoa,
#        arquivo,
#        indent=2)

with open('aula59.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    #print(pessoa)
    #print(type(pessoa))