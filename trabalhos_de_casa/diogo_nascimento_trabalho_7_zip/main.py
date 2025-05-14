from funcoes import *
from funcoes import cadastrar_produto, listar_produtos, vender_produto, listar_vendas

def menu():
    while True:
        print("\n--- Loja Python ---")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Realizar venda")
        print("4. Listar vendas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            estoque = int(input("Quantidade em estoque: "))
            cadastrar_produto(nome, preco, estoque)

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