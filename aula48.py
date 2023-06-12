# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterando
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

def inverter_string(string):
    return string[::-1]


invertida = inverter_string('Lucas')

print(invertida)