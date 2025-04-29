from funcoes import *
import globais

limpa()

opcao = None

while(opcao != 0):
  opcao = exibir_menu()

  animar("Aguarde")

  if(opcao == 1): registar_venda()
  elif(opcao == 2): cancelar_venda()
  elif(opcao == 3): verificar_vendas()
  elif(opcao == 0): 
    animar("A sair")
    print(f"{globais.empresa} agradece sua contribuição.")
  else: print("--- OPÇÃO INVÁLIDA ---\n")

  prima_enter()

print("\n\n")