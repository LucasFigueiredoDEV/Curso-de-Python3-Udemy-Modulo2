'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
'''

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
#retorna os valores das variaveis definidas dentro do escopo
#mesmo que a variável de dentro do escopo seja igual à variavel de 
#fora, todas as variáveis definidas dentro, são exclusivas do escopo.
print(x)