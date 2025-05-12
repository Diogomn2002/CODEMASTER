from funcoes import *

limpa()

# vetor = []
dicionario = {
  "nome": "Fabrício",
  "idade": 29,
  "morada": "Covilhã"
}
# matriz_de_vetores = [[], [], []]
# matriz_de_dicionarios = [{}, {}, {}]

print(f"Dicionário original: {dicionario}\n")

print("=== Dicionário com FOR ===\n")
for info in dicionario:
  print(f"{info}: {dicionario[info]}")

print("\n=== Dicionário apenas as chaves ===\n")
print(dicionario.keys())

print("\n=== Dicionário apenas os valores ===\n")
print(dicionario.values())

print("\n\n")