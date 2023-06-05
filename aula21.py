# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #Une os dois sets com "|"
s3 = s1 & s2 #Faz a interceção entre os dois sets, ou seja, vai mostrar o que tem os nos dois sets simultâneamente.
s3 = s1 - s2 #Mostra os valores que estão presentes apenas no s1
s3 = s2 - s1 #Mostra os valores que estão presentes apenas no s2
s3 = s2 ^ s1 #Mostra a diferença simétrica, ou seja vai mostrar os itens que estão presentes unicamente em ambos, ou seja o 1 e 4. (A ordem do código não importa nesse caso)
print(s3)