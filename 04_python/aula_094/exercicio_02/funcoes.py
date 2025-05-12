import os
import time
import globais

# Funções
def exibir_menu():
  animar("Aguarde")
  print("=== Gestão de Colaboradores ===\n")
  print("1 - Novo colaborador.")
  print("2 - Editar colaborador.")
  print("3 - Apagar colaborador.\n")
  print("4 - Listar todos os colaboradores.\n")
  print("0 - Sair.\n")
  return int(input("- Opção: "))

def registar():
  print("--- Novo Colaborador ---\n")
  nome = input("- Digite o NOME do novo colaborador(a): ")
  cargo = input("- Digite o CARGO do novo colaborador(a): ")
  ordenado = float(input("- Digite o ORDENADO do novo colaborador(a): "))
  # novo_colaborador = [nome, cargo, ordenado]
  # novo_colaborador = {"nome": nome, "cargo": cargo, "ordenado": ordenado}
  novo_colaborador = criar_colaborador(nome, cargo, ordenado)
  globais.colaboradores.append(novo_colaborador)
  print("\n--- SUCESSO! ---")

def editar():
  print("--- Editar Colaborador ---\n")
  listar(False)
  linha = int(input("\n- Digite o ID do colaborador a ser editado: "))
  print()

  if(linha >= 0 and linha < len(globais.colaboradores)):
    c = globais.colaboradores[linha]

    print("--- Editar ---\n")
    print("1 - Nome.")
    print("2 - Cargo.")
    print("3 - Ordenado.\n")
    print("0 - Cancelar.\n")
    coluna = int(input("- Opção: ")) - 1

    print()

    if(coluna == 0):
      c["nome"] = input(f"- Digite o NOME que substituirá ({c['nome']}): ")
      print("\n--- SUCESSO! ---")

    elif(coluna == 1):
      c['cargo'] = input(f"- Digite o CARGO que substituirá ({c['cargo']}): ")
      print("\n--- SUCESSO! ---")

    elif(coluna == 2):
      c['ordenado'] = float(input(f"- Digite o ORDENADO que substituirá ({c['ordenado']:.2f} €): "))
      print("\n--- SUCESSO! ---")

    elif(coluna == -1): print("--- OPERAÇÃO CANCELADA! ---")
    
    else: print("--- OPÇÃO INVÁLIDA! ---")

  else: print("--- ID INVÁLIDO! ---")


def apagar():
  print("--- Apagar Colaborador ---\n")
  listar(False)
  linha = int(input("\n- Digite o ID do colaborador a ser apagado: "))
  print()
  if(linha >= 0 and linha < len(globais.colaboradores)):
    print(f"--- ( {globais.colaboradores[linha]['nome']} ) APAGADO(A) COM SUCESSO! ---")
    globais.colaboradores.pop(linha)
  else: print("--- ID INVÁLIDO! ---")

def listar(com_titulo):
  if(com_titulo): print("--- Lista dos Colaboradores ---\n")

  soma_total = 0
  for i in range(len(globais.colaboradores)):
    linha = globais.colaboradores[i]
    print(f"(ID: {i}) | (Nome: {linha['nome']}) | (Cargo: {linha['cargo']}) | (Ordenado: {linha['ordenado']:.2f} €)")
    soma_total += linha['ordenado']
  
  if(com_titulo): 
    print(f"\nTotal de colaboradores: ({len(globais.colaboradores)})")
    print(f"Ordenado total mensal da equipa: ({soma_total:.2f} €)")


def criar_colaborador(nome, cargo, ordenado):
  dicionario = {
    "nome": nome,
    "cargo": cargo,
    "ordenado": ordenado,
  }
  return dicionario

def init():
  globais.colaboradores.append(criar_colaborador("Fabrício Vidal", "Formador", 100))
  globais.colaboradores.append(criar_colaborador("Maria Silva", "Médica", 500))
  globais.colaboradores.append(criar_colaborador("Ana Sousa", "Vendas", 400))



