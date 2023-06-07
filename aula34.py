# dir, hasattr e getattr em Python

string = 'Lucas'
metodo = 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)