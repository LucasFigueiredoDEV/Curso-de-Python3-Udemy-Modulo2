# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s1) #O set retira valores repitidos, o que pode ser muito util.
# O problema do set, é que ele não garante a ordem dos itens.

