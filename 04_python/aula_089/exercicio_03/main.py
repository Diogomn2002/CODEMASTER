from funcoes import *

limpa()

lista = []

# animar("Aguarde")

for i in range(int(input("- Digite a quantidade de alunos que serão cadastrados: "))):
  lista.append(input(f"- Digite o nome do(a) [{i+1}º] aluno(a): "))

# animar("Aguarde")

lista.sort()

print("\n=== Lista de Alunos Ordenada ===\n")
for i in range(len(lista)): print(f"{i+1} - {lista[i]}.")


print("\n\n")