from funcoes import *

limpa()

opcao = ""

while(opcao.lower() != "x"):

  opcao = exibir_menu()

  animar("Aguarde", 0.2)

  if(opcao.lower() == "a"): registar()
  elif(opcao.lower() == "b"): remover()
  elif(opcao.lower() == "c"): listar()
  elif(opcao.lower() == "x"): animar("A sair", 0.2)
  else: print("--- OPÇÃO INVÁLIDA ---")

  aguarde(3)


print("\n\n")