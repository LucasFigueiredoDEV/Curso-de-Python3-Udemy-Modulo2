# Funções recursivas e recursividade
# - FDunções que podem se chamar de volta
# - Úteis para dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - Fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial

def recursiva(inicio=0, fim=4):
    print(inicio, fim)


    # Caso base
    if inicio >= fim:
        return fim
    
    # Caso recursivo
    # Contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())