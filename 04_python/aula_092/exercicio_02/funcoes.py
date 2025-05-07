import os
import time
import globais

# Funções
def exibir_menu():
  animar("Aguarde")
  print("=== Menu ===\n")
  print("1 - Cadastrar pessoa.")
  print("2 - Editar pessoa.")
  print("3 - Apagar pessoa.\n")
  print("4 - Listar todas as pessoas.\n")
  print("0 - Sair.\n")
  return int(input("- Opção: "))

def cadastrar():
  print("--- Cadastro de Pessoa ---\n")
  nome = input("- Digite o NOME da nova pessoa: ")
  idade = int(input("- Digite a IDADE da nova pessoa: "))
  morada = input("- Digite a MORADA da nova pessoa: ")
  nif = int(input("- Digite o NIF da nova pessoa: "))
  nova_pessoa = [nome, idade, morada, nif]
  globais.pessoas.append(nova_pessoa)
  print("\n--- SUCESSO! ---")

def editar(): 
  print("--- Editar Pessoa ---\n")
  listar(False)
  print()
  linha = int(input("- Digite o ID da pessoa a ser editada: ")) - 1
  if(linha >= 0 and linha < len(globais.pessoas)):
    print("\n--- Editar ---\n")
    print("1 - Editar NOME.")
    print("2 - Editar IDADE.")
    print("3 - Editar MORADA.")
    print("4 - Editar NIF.\n")
    print("0 - Cancelar.\n")
    coluna = int(input("- Opção: ")) - 1
    print()
    if(coluna == 0):
      globais.pessoas[linha][coluna] = input("- Digite o novo NOME: ")
      print("\n--- SUCESSO! ---")
    elif(coluna == 1):
      globais.pessoas[linha][coluna] = input("- Digite a nova IDADE: ")
      print("\n--- SUCESSO! ---")
    elif(coluna == 2):
      globais.pessoas[linha][coluna] = input("- Digite a nova MORADA: ")
      print("\n--- SUCESSO! ---")
    elif(coluna == 3):
      globais.pessoas[linha][coluna] = input("- Digite a nova NIF: ")
      print("\n--- SUCESSO! ---")
    elif(coluna == -1): print("\n--- OPERAÇÃO CANCELADA! ---")
    else: print("\n--- OPÇÃO INVÁLIDA! ---")

def apagar(): 
  print("--- Apagar Pessoa ---\n")
  listar(False)
  print()
  linha = int(input("- Digite o ID da pessoa a ser apagada: ")) - 1
  if(linha >= 0 and linha < len(globais.pessoas)):
    globais.pessoas.pop(linha)
    print("\n--- SUCESSO! ---")
  else: print("\n--- ID INVÁLIDO ---")


def listar(com_titulo):
  if(com_titulo): print("--- Lista de Todas as Pessoas ---\n")
  for i in range(len(globais.pessoas)):
    p = globais.pessoas[i]
    print(f"{i+1} - {p[0]} (Idade: {p[1]}) (Morada: {p[2]}) (NIF: {p[3]})")

