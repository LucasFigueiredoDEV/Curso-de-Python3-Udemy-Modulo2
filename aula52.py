# Count é um iterador sem fim (itertools)

from itertools import count


c1 = count(step = 8, start= 8) #No count só se passa como parâmetro, o start e o step, e ele contará até o infinito

r1 = range(8, 100, 8)# O range se passa, o start, end e step, e ele será definido do inicio ao fim com os passos indicados


print('count')

for i in c1:
    if i > 100:
        break
    print(i)


print()
print('Range')
for i in r1:
    print(i)