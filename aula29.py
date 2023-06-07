import pprint #modulo para printar mais organizada


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40) #parâmetros que se deve passar


# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
    for produto in produtos if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]#para utlizar um filtro, deve-se utilizar um if logo após o for
p(novos_produtos)