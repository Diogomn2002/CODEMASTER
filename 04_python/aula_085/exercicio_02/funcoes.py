import globais
import os
import time

# Funções
def exibir_menu():
  animar("Aguarde")
  print(f"=== {globais.empresa} ===\n")
  print("1 - Registar venda.")
  print("2 - Cancelar venda.")
  print("3 - Verificar vendas.\n")
  print("0 - Logout.\n")
  opcao = int(input("Opção: "))
  return opcao

def registar_venda():
  print(f"--- {globais.empresa} (Registar Venda) ---\n")
  valor = float(input("- Digite o valor da venda: "))
  globais.soma_total_vendas += valor
  print("\n--- SUCESSO! ---")

# def registar_venda_especial():
#   print(f"--- {globais.empresa} (Registar Venda) ---\n")
#   resposta = ""
#   while(resposta.lower() != "nao"):
#     valor = float(input("- Digite o valor da venda: "))
#     globais.soma_total_vendas += valor
#     resposta = input("- Desejas registar mais um produto? ")
#   print("\n--- SUCESSO! ---")

def cancelar_venda():
  print(f"--- {globais.empresa} (Cancelar Venda) ---\n")
  valor = float(input("- Digite o valor da venda a ser cancelada: "))
  globais.soma_total_vendas -= valor
  print("\n--- SUCESSO! ---")

def verificar_vendas():
  print(f"--- {globais.empresa} (Verificar Vendas) ---\n")
  print(f"Valor total das vendas: ( {globais.soma_total_vendas:.2f} € )")

