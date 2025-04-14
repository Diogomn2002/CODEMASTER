from funcoes import *

limpa()

opcao = exibir_menu()

animar("A analisar", 0.3)

if(opcao.lower() == "t"): calcular_triangulo()
elif(opcao.lower() == "r"): calcular_rectangulo()
elif(opcao.lower() == "c"): calcular_circulo()
else:
  print("===== Cálculo de Áreas com Funções =====\n")
  print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")