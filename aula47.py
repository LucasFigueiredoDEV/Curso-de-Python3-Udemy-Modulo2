# Variáveis livres + nonlocal (locals, globals)

#def fora(x):
#    a = x
#
#    def dentro():
#        print(locals())
#        return a # Esse conceito é dado, porque a variável "a" não está definida dentro do escopo da função "dentro"
#    # mas a mesma pode ser retornada dentro do escopo da função "dentro".
#    return dentro

#dentro1 = fora(10)
#dentro2 = fora(20)

#print(dentro1())
#print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar = ''):
        nonlocal valor_final
        valor_final += valor_a_concatenar #A variável livre só pode ser lida e não manipulada, mas para que eu consiga manipular
        # deve-se informar ao python que a variável não está definida nesse escopo, utilizando nonlocal, fazendo com que ele procure a variável em escopos acima
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)