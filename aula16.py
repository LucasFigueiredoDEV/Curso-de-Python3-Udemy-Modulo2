# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Lucas Samuel',
    'sobrenome': 'Figueiredo',
}

print(p1.get('nome', 'não existe')) #obtem o valor da chave, e caso ela não exista irá exibir o segundo valor dentro do get
nome = p1.pop('nome') #deleta do dicionário, mas ao printar com a variável "nome", o valor será impresso.
print(nome)
print(p1)

ultima_chave = p1.popitem() #deleta a ultima chave do dicionário.
print(nome)
print(p1)

p1.update({
#Update atualiza o dicionário, ou seja, o valor que for definido dentro do update, passará a ser o novo valor no dicionário.
    'nome': 'Novo valor',
    'idade': 20,
    #Além de atulizar valores, também é possível adicionar novas chaves ao dicionário.
})
p1.update(nome = 'novo valor', idade = 20) #Uma outra forma mais simples de utilizar o update.
print(p1)