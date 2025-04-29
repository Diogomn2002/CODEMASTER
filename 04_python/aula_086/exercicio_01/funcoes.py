import globais
import os
import time

# Funções
def exibir_menu():
  animar("Aguarde")
  print("=== Multibanco Python ===\n")
  print(f"Contar: {globais.conta}")
  print(f"Saldo: {globais.saldo:.2f} €\n")
  print("1 - Levantamentos.")
  print("2 - Depósitos.")
  print("3 - Pagamentos.\n")
  print("4 - Sair.\n")
  return int(input("- Opção: "))

def levantar():
  print("--- Levantamentos ---\n")
  valor = float(input("- Digite o valor a ser levantado: "))
  print()
  if(valor > 0 and valor <= globais.saldo):
    globais.saldo -= valor
    print("--- SUCESSO! ---")
  else: print("--- VALOR INVÁLIDO! ---")

def depositar():
  print("--- Depósitos ---\n")
  valor = float(input("- Digite o valor a ser depositado: "))
  print()
  if(valor > 0):
    globais.saldo += valor
    print("--- SUCESSO! ---")
  else: print("--- VALOR INVÁLIDO! ---")

def pagar():
  print("--- Pagamentos ---\n")
  descricao = input("- Digite a descrição do pagamento: ")
  valor = float(input("- Digite o valor a ser pago: "))
  print()
  if(valor > 0 and valor <= globais.saldo):
    globais.saldo -= valor
    print("--- SUCESSO! ---")
  else: print("--- VALOR INVÁLIDO! ---")
