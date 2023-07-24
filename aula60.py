# Problema dos parâmetros mutáveis em funções Python

def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista



cliente1 = adiciona_cliente('Lucas')
adiciona_cliente('Ana', cliente1)


cliente2 = adiciona_cliente('Helena')
adiciona_cliente('Maria', cliente2)


cliente3 = adiciona_cliente('Luiza')
adiciona_cliente('Vivi', cliente3)



print(cliente1)
print(cliente2)
print(cliente3)