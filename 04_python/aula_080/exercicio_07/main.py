from funcoes import *

limpa()


print("A analisar", end="", flush=True)
aguarde(0.2)

loop = 1
while(loop <= 20):
  print(".", end="", flush=True)
  aguarde(0.1)
  loop += 1


print("\n\n")