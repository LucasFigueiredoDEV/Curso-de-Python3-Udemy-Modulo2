# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro.

def operacoes(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = operacoes(2)
triplicar = operacoes(3)
quadruplicar = operacoes(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

