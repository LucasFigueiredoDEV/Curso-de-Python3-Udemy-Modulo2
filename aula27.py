# List comprehension Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
] #modo de utilizar a list comprehension
print(lista)