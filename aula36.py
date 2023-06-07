import sys


# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterador = iter(iterable) #tem __iter__e__next__
lista = [n for n in range(100)]
generator = (n for n in range(100))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)