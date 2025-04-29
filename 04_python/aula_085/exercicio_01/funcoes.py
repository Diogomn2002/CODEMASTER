import globais
import os
import time

# Funções
def exibir_menu():
  animar("Aguarde", 0.2)
  print("=== MENU ===\n")
  print("A - Registar colaborador.")
  print("B - Remover colaborador.")
  print("C - Verificar estatísticas.")
  print("X - Sair.\n")
  opcao = input("Opção: ")
  return opcao

def registar():
  print("--- Registo de Colaborador ---\n")
  nome = input("- Digite o nome do novo colaborador: ")
  ordenado = float(input("- Digite o ordenado deste colaborador: "))
  globais.soma_total += ordenado
  globais.total_colaboradores += 1
  print("\n--- SUCESSO ---")

def remover():
  print("--- Remover ordenado do Colaborador ---\n")
  ordenado = float(input("- Digite o ordenado deste colaborador que saiu: "))
  globais.soma_total -= ordenado
  globais.total_colaboradores -= 1
  print("\n--- SUCESSO ---")

def listar():
  media = 0
  if(globais.total_colaboradores > 0): media = globais.soma_total / globais.total_colaboradores
  print("--- Estatíticas da Empresa ---\n")
  print(f"Total de ordenado mensal: ( {globais.soma_total:.2f} € )")
  print(f"Ordenado médio por colaborador: ( {media:.2f} € )")


