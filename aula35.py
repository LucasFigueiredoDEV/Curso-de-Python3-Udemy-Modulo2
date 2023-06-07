# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterador = iterable.__iter__() #tem __iter__e__next__
print(next(iterador))
print(next(iterador))
print(next(iterador))