'''
Higher Order Functions
Funções de primeira classe
'''
def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args): #Chamando uma função, dentro de outra função. Funções possibilitam fazer varias coisas.
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)