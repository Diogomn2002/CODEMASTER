from funcoes import *

limpa()

resposta_1 = input("- Desejas tirar a carta de condução? ")

if(resposta_1.lower() == "sim"):

  tentativas = 1
  resposta_2 = ""
  while(resposta_2.lower() != "sim"):
    print(f"\nEstudar para o ({tentativas}°) teste.")
    resposta_2 = input(f"- Você passou no o ({tentativas}°) teste? ")
    tentativas += 1

  print("\nParabéns!")
  print(f"Fostes aprovado no ({tentativas-1}°) teste.")
  
else: print("\nEntão utilize transportes públicos.")


print("\n\n")