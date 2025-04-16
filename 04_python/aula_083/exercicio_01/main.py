from funcoes import *

limpa()

print("\n==== Maior e Menos Número ====\n ")

total = float(input("-Digite o total de números que serão analisados: "))

loop = 1
maior = None
menor = None

while loop <= total:
  numero = int(input(f"- Digite o [{loop}] número: "))
  
  if maior is None or numero > maior:
    maior = numero

  if menor is None or numero < menor:
    menor = numero

  loop += 1

#Resultado Final
print(f"--- O maior número digitado foi: ({maior}) ---")
print(f"--- O menor número digitado foi: ({menor}) ---")

print("\nFIM")


print("\n\n")