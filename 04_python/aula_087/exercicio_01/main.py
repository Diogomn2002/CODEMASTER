from funcoes import *

limpa()

opcao = None
while(opcao != 0):

  opcao = exibir_menu()

  animar("Aguarde")

  if(opcao == 1): vender()
  elif(opcao == 2): exibir_historico()
  elif(opcao == 0): animar("Sair")
  else: print("--- OPÇÃO INVÁLIDA ---")

  prima_enter()



print("\n\n")