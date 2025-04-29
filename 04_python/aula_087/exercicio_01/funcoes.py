import globais
import os
import time

# Funções
def exibir_menu():
  animar("Aguarde")
  print("=== Padaria do Python ===\n")
  print("1 - Vender.")
  print("2 - Ver histórico.")
  print("0 - Sair.\n")
  return int(input("- Opção: "))

def vender():
  print("--- Vender ---\n")
  descricao = input("- Descrição da venda: ")
  valor = float(input("- Valor total da venda: "))
  print()
  if(valor > 0):
    globais.saldo_total += valor
    globais.historico += f"{globais.id} - {descricao} - {valor:.2f} €\n"
    globais.id += 1
    print("--- SUCESSO! ---")
  else: print("--- VALOR INVÁLIDO! ---")

def exibir_historico():
  print("--- Histórico ---\n")
  print(f"Total das vendas: {globais.saldo_total:.2f} €\n")
  print(globais.historico)

