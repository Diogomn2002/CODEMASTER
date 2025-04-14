import os
import time
import math

# Funções
def calcular_triangulo():
  base = float(input("- Digite a base do triângulo: "))
  altura = float(input("- Digite a altura do triângulo: "))
  area = base * altura / 2
  animar("A analisar", 0.3)
  print("===== Cálculo de Áreas com Funções =====\n")
  print(f"--- A área do triângulo é de ({area:.1f}) ---")

def calcular_rectangulo():
  base = float(input("- Digite a base do rectângulo: "))
  altura = float(input("- Digite a altura do rectângulo: "))
  area = base * altura
  animar("A analisar", 0.3)
  print("===== Cálculo de Áreas com Funções =====\n")
  print(f"--- A área do rectângulo é de ({area:.1f}) ---")

def calcular_circulo():
  raio = float(input("- Digite o raio do círculo: "))
  area = math.pi * raio ** 2
  animar("A analisar", 0.3)
  print("===== Cálculo de Áreas com Funções =====\n")
  print(f"--- A área do círculo é de ({area:.1f}) ---")

def exibir_menu():
  print("===== Cálculo de Áreas com Funções =====\n")
  print("--- Escolha uma opção ---\n")
  print("(t) - para triângulos.")
  print("(r) - para rectângulos.")
  print("(c) - para círculos.\n")
  opcao = input("Opção: ")
  return opcao









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