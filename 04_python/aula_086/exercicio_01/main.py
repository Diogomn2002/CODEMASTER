from funcoes import *

limpa()

opcao = None
while(opcao != 4):
  
  opcao = exibir_menu()
  
  animar("Aguarde")

  if(opcao == 1): levantar()
  elif(opcao == 2): depositar()
  elif(opcao == 3): pagar()
  elif(opcao == 4): animar("A sair")
  else: print("--- OPÇÃO INVÁLIDA! ---")

  prima_enter()


print("\n\n")