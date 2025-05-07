from funcoes import *

limpa()

pessoas = [
  ["Fabrício", 28, "Covilhã"],
  ["Maria", 14, "Lisboa"],
  ["Ana", 56, "Amadora"],
  ["Carlos", 44, "Porto"],
]

print(pessoas)

print()

nome = input("- Digite um nome: ")
idade = int(input("- Digite uma idade: "))
morada = input("- Digite uma morada: ")
nova_pessoa = [nome, idade, morada]
pessoas.append(nova_pessoa)

print()

print(pessoas)

# pessoas = ["fabricio", "maria", "joao"]

# nome = input("- Digite o nome da nova pessoa: ")
# pessoas.append(nome)

# print(pessoas)

print("\n\n")