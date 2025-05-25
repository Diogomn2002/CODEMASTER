from funcoes import *
from funcoes import cadastrar_produto, listar_produtos, vender_produto, listar_vendas

def menu():
    while True:
        print("\n=== Loja Python ===\n")
        print("1 - Registrar produto.")
        print("2 - Editar produto.")
        print("3 - Apagar produto.")
        print("4 - Listar produtos.\n")
        print("5 - Vender.")
        print("6 - Listar vendas.\n")
        print("0. Sair\n")
        opcao = input("Opção: ")

        if opcao == "1":
            print("--- Registar Produto ---\n")
            nome = input("- Digite o nome do novo produto: ")
            preco = float(input("- Digite o preço deste produto: "))
            quantidade = int(input("- Digite a quantidade deste produto: \n"))
            cadastrar_produto(nome, preco, quantidade)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            listar_produtos()
            indice = int(input("Número do produto a vender: ")) - 1
            quantidade = int(input("Quantidade: "))
            vender_produto(indice, quantidade)

        elif opcao == "4":
            listar_vendas()

        elif opcao == "0":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()


limpa()

init()

opcao = None
while(opcao != 0):

  opcao = exibir_menu()

  animar("Aguarde")

  if(opcao == 1): registar()
  elif(opcao == 2): editar()
  elif(opcao == 3): apagar()
  elif(opcao == 4): listar(True)
  elif(opcao == 0): animar("A sair")
  else: print("--- OPÇÃO INVÁLIDA! ---")

  prima_enter()

print("\n\n")