# Dictionary Comprehension e Set Comprehension

produto = {
    'nome' : 'Caneta Azul',
    'preco' : 2.5,
    'categoria' : 'desenho',
}

dc = {
    chave: valor.upper()
     if isinstance(valor, str)#Checka se o valor é uma str para que possa aplicar o método uppr, caso não seja ele só imprime o valor padrão
     else valor for chave, valor in produto.items
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]


dc1 = {
    chave:valor 
    for chave, valor in lista
}
print(dc)