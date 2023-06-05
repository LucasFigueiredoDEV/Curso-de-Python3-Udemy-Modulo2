# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Lucas') #add - adciona ao set o que for passado entre parênteses.
s1.add(50)
s1.update('Olá mundo') #update adciona ao set, mas de forma iterada(Ou seja, separada letra por letra), além de que pode ser utilizado para mandar vários valores ao mesmo tempo.
s1.update(('Olá', 1, 2, 3, 4, 5))
#s1.clear() #limpa o set
s1.discard('Olá mundo')#Elimina um valor de dentro do set, mas o valor deverá ser escrito, pois não há a posssibiliade de saber o índice do valor.

print(s1)
