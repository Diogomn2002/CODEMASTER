from funcoes import *

limpa()

# 1 Coluna = nome
# 2 Coluna = morada
# 3 Coluna = idade
# 4 Coluna = saldo bonus
# 5 Coluna = peso
# 6 Coluna = altura
# 7 Coluna = nome do pai
# 8 Coluna = nome do mae
matriz = [
  ["fabricio", "covilha", 29, 88.10, 89.15, 1.92, "fabricio", "maria"],
  ["maria", "lisboa", 55, 0, 55.2, 1.55, "andre", "marta"],
  ["carlos", "almada", 67, 10, 55.8, 1.88, "gabriel", "alice"]
]

pessoa_individual_vetor = ["fabricio", "covilha", 29, 88.10, 89.15, 1.92, "fabricio", "maria"]
pessoa_individual_dicionario = {
  "nome": "fabricio",
  "morada": "covilha",
  "idade": 29,
  "saldo_bonus": 88.10,
  "peso": 89.15,
  "altura": 1.92,
  "nome_pai": "fabricio",
  "nome_mae": "maria"
}

print(pessoa_individual_vetor[4])

print(pessoa_individual_dicionario["peso"])
print(pessoa_individual_dicionario["nome_mae"])

print("="*20)

matriz_2 = [
  {"nome": "fabricio", "morada": "covilha", "idade": 29, "saldo_bonus": 88.10},
  {"nome": "maria", "morada": "lisboa", "idade": 56, "saldo_bonus": 20},
  {"nome": "jose", "morada": "almada", "idade": 18, "saldo_bonus": 5}
]

for i in range(len(matriz)):
  linha = matriz[i]
  print(f"{linha[0]} - (Morada: {linha[1]}) (Idade: {linha[2]})")

print("="*20)

for i in range(len(matriz_2)):
  linha = matriz_2[i]
  print(f"{linha['nome']} - (Morada: {linha['morada']}) (Idade: {linha['idade']})")

print("="*20)

print(pessoa_individual_dicionario.keys())
print(pessoa_individual_dicionario.values())

print("="*20)

for i in pessoa_individual_dicionario.keys():
  print(i)

print("="*20)

for i in pessoa_individual_dicionario.values():
  print(i)

print("="*20)

print(pessoa_individual_dicionario["morada"])

print("="*20)

for i in pessoa_individual_dicionario:
  print(f"{i} - {pessoa_individual_dicionario[i]}")

print("\n\n")