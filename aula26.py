# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)
#a, b = pessoa.values()
#print(a, b)

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Figueiredo',
}

dados_pessoa = {
    'idade' : 20,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoa}
#print(pessoa_completa)

#args e kwargs
# args (já foi visto)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
