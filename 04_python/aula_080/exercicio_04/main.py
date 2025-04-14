from funcoes import *

limpa()


print("=== INÍCIO ===\n")

print("Estudar para teste")
print("Fazer para teste")
print()
resposta = input("Você passou no teste? ")

print()

if(resposta.lower() == "sim"): print("Pegar carta")
else:
  print("Estudar para teste")
  print("Fazer para teste")
  print()
  resposta = input("Você passou no teste? ")
  if(resposta.lower() == "sim"): print("Pegar carta")
  else:
    print("Estudar para teste")
    print("Fazer para teste")
    print()
    resposta = input("Você passou no teste? ")

print("\n=== FIM ===")


print("\n\n")