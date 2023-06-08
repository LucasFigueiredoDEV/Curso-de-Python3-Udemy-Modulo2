# try, except, else e finally
# Try pode ser utilizado com except, e com 
#finally, mas não pode se utilizado sozinho com o else.
# Except pode ser utilizado quantas vezes for necessário.
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:# Finally sempre vai ser executado, mesmo que ocorra um erro no meio do código
    print('FECHAR ARQUIVO')
