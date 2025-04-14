from funcoes import *

limpa()

numero = int(input("- Digite um número inteiro positivo: "))

print()

print("=== Exercício Principal ===\n")
loop = 1
while(loop <= numero):
  print(loop)
  loop += 1


print("\n\n=== Desafio ===\n")
loop_2 = numero
while(loop_2 >= 1):
  print(loop_2)
  loop_2 -= 1

print(f"\n\n\nO número digitado foi ({numero})")

print("\n\n")