
# O programa em Python calcula e mostra a média de três notas de um aluno.
# para armazenar valores em variáveis ou espaços de memórias.

# Entrada variaveis notas

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
faltas = int(input("Número de faltas: "))
# Processamento
media = (n1 + n2 + n3 ) / 3

# Saida
print("A media é:", media)


print("-----------------------------------------------------")
if (media>=6 and faltas<25):
    print("Parabéns, aluno aprovado!")
else:
    print("Reprovado")

print("-----------------------------------------------------")
