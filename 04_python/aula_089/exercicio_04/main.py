from funcoes import *
import random

limpa()

total = int(input("- Digite o total de nomes completos aleatórios que você deseja gerar: "))

nomes = ["fabricio", "maria", "ana", "jose", "carlos", "bruno"]
apelidos = ["vidal", "matos", "silva", "sousa", "ferreira", "veloso", "vieira"]

print()

for i in range(total):
  n = random.randint(0, len(nomes)-1)
  a = random.randint(0, len(apelidos)-1)
  print(f"{i+1} - {nomes[n]} {apelidos[a]}.")


print("\n\n")