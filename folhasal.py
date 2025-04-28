# Função para calcular o aumento nos salários
def calcularAumento(salarios, percentual):
    novos_salarios = []
    for salario in salarios:
        aumento = salario * (percentual / 100)
        novos_salarios.append(salario + aumento)
    return novos_salarios

# Função para calcular a soma de uma lista
def somaLista(lista):
    return sum(lista)

# Programa principal
salariosOriginais = [1500, 2000, 1200, 3000, 2700]
novosSalarios = calcularAumento(salariosOriginais, 4.5)
Soma1 = somaLista(salariosOriginais)
Soma2 = somaLista(novosSalarios)
impactoFolha = Soma2 - Soma1

print(novosSalarios)
print("Aumento na Folha: ", impactoFolha)
