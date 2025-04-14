from funcoes import *

limpa()

resposta_1 = ""
while(resposta_1.lower() != "sim" and resposta_1.lower() != "nao"):
  resposta_1 = input("- Desejas tirar a carta de condução? ")
  if(resposta_1.lower() != "sim" and resposta_1.lower() != "nao"):
    print("\nResponda apenas com 'sim' ou 'nao'.\n")

if(resposta_1.lower() == "sim"):

  tentativas = 0
  resposta_2 = "nao"
  while(resposta_2.lower() != "sim"):
    if(resposta_2.lower() != "nao"): print("\nResponda apenas com 'sim' ou 'nao'.")
    else: tentativas += 1
    print(f"\nEstudar para o ({tentativas}°) teste.")
    resposta_2 = input(f"- Você passou no o ({tentativas}°) teste? ")

  print("\nParabéns!")
  print(f"Fostes aprovado no ({tentativas}°) teste.")
  
else: print("\nEntão utilize transportes públicos.")


print("\n\n")