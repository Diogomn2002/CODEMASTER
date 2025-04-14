from funcoes import *

limpa()

print("===== Cálculo de Áreas com Funções =====\n")
print("--- Escolha uma opção ---\n")
print("(t) - para triângulos.")
print("(r) - para rectângulos.")
print("(c) - para círculos.\n")

opcao = input("Opção: ")

animar("A analisar", 0.3)

if(opcao.lower() == "t"): calcular_triangulo()
elif(opcao.lower() == "r"): calcular_rectangulo()
elif(opcao.lower() == "c"): calcular_circulo()
else:
  print("===== Cálculo de Áreas com Funções =====\n")
  print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")