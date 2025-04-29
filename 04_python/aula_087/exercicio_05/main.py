from funcoes import *

limpa()

produtos = ["caderno", "x-acto", "caneta", "bolsa", "lapis", "borracha"]
print(produtos)

print()
print("="*20)
print()

produtos.sort()
print(produtos)

print()
print("="*20)
print()

produtos.sort(reverse=True)
print(produtos)

print()
print("="*20)
print()

if("papel" in produtos): print("Sim")
else: print("Não")

print()
print("="*20)
print()

turma_1 = ["maria", "jose", "joao"]
turma_2 = ["fabricio", "carlos", "mario"]
escola = turma_1 + turma_2
print(escola)

print()
print("="*20)
print()

turma_1.extend(turma_2)
print(turma_1)

print()
print("="*20)
print()

turma_1.clear()
print(turma_1)

print("\n\n")