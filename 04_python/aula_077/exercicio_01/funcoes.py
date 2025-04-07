import os

def calcular_dobro(numero):
  resultado = numero *2
  print("O dobro de ( {numero} ) é ( {resultado} )")





# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")