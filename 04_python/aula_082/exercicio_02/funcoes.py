import os
import time

# Funções
def contador_numeros():
  total_numeros = int(input("- Digite o total de números que serão analisados: "))
  
pares = 0
impares = 0
loop = 1
  
while loop <= total_numeros:
  numero = int(input(f"- Digite o ({loop}º) número: "))
      
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1
      
  loop += 1
  
print(f"\n--- Total de números PARES: ({pares}) ---")
print(f"--- Total de números ÍMPARES: ({impares}) ---")


# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(segundos): time.sleep(segundos)

def animar(frase, tempo):
  limpa()
  print(frase, end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  limpa()