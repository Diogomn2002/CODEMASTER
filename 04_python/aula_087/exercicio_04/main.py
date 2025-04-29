from funcoes import *

limpa()

produtos = ["caderno", "caneta", "bolsa", "lapis", "borracha"]
print(produtos)

print()
print("="*20)
print()

produtos.append("papel")
print(produtos)

print()
print("="*20)
print()

produtos.insert(1, "x-acto")
print(produtos)

print()
print("="*20)
print()

produtos.pop()
print(produtos)

print()
print("="*20)
print()

produtos.pop(1)
print(produtos)

print()
print("="*20)
print()

produtos.remove("lapis")
print(produtos)

print()
print("="*20)
print()

del produtos[0:10]
# nova_lista = produtos[0:10] + produtos[25:53]
print(produtos)

print("\n\n")