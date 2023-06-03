#Exercicios com funções


#Crie uma função que multiplica todos os argumentos
#não nomeados recebidos
#Retorne o total para uma variável e mostre o valor da variável

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)



#Crie uma função que fala se um número é par ou ímpar.
#Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return ('{} é par!'.format(numero))
    return ('{} é impar!'.format(numero))
while True:
    try:
        valores_pedidos = input('Digite um valor para saber se ele é par ou ímpar: ')
        valores_pedidos_int = int(valores_pedidos)
        print(par_impar(valores_pedidos_int))
    except:
        break
print('Acabou!')