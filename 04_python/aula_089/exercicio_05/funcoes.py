import os
import time
import globais

# Funções
def exibir_menu():
  animar("Aguarde")
  print("=== Biblioteca da Covilhã ===\n")
  print("1 - Registar livro.")
  print("2 - Editar livro.")
  print("3 - Apagar livro.")
  print("4 - Listar todos os livros.\n")
  print("0 - Sair.\n")
  return int(input("- Opção: "))

def registar():
  print("--- Registar Livro ---\n")
  novo_livro = input("- Digite o nome do novo livro: ")
  globais.livros.append(novo_livro)
  print("\n--- SUCESSO! ---")

def editar():
  print("--- Editar Livro ---\n")
  listar(False)
  id = int(input("\n- Digite o ID do produto a ser editado: ")) - 1
  if(id >= 0 and id < len(globais.livros)):
    globais.livros[id] = input("- Digite o novo nome: ")
    print("\n--- SUCESSO! ---")
  else: print("\n--- ID INVÁLIDO! ---")

def apagar():
  print("--- Apagar Livro ---\n")
  listar(False)
  id = int(input("\n- Digite o ID do produto a ser apagado: ")) - 1
  if(id >= 0 and id < len(globais.livros)):
    globais.livros.pop(id)
    print("\n--- SUCESSO! ---")
  else: print("\n--- ID INVÁLIDO! ---")


def listar(com_titulo):
  if(com_titulo == True): print("--- Lista dos Livros ---\n")
  for i in range(len(globais.livros)):
    print(f"{i+1} - {globais.livros[i]}")
