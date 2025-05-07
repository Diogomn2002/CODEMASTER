from funcoes import *

limpa()

total = int(input("- Digite a quantidade de alunos que serão cadastrados: "))
lista = []

animar("Aguarde")

for i in range(total):
  novo_aluno = input(f"- Digite o nome do(a) [{i+1}º] aluno(a): ")
  lista.append(novo_aluno)

animar("Aguarde")

lista.sort()

print("=== Lista de Alunos Ordenada ===\n")
for i in range(total): print(f"{i+1} - {lista[i]}.")


print("\n\n")