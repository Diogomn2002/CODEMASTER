from funcoes import *

limpa()

frutas = ['uva', 'maçã', 'morango', 'ananás', 'banana', 'laranja']

print(f"Lista original: {frutas}")

print("\n=== Lista de Frutas com FOR ===\n")
for f in frutas: print(f)

print("\n=== Lista de Frutas com FOR + RANGE() ===\n")
for i in range(len(frutas)): print(f"{i+1} - {frutas[i]}")

print("\n=== Lista de Frutas com FOR + REVERSE() ===\n")
for f in reversed(frutas): print(f)

print("\n=== Lista de Frutas com FOR + RANGE() Reverso ===\n")
for i in range(len(frutas)-1, -1, -1): print(f"{i+1} - {frutas[i]}")

print("\n=== Lista de Frutas com FOR + RANGE() Reverso exemplo 2 ===\n")
for i in reversed(range(len(frutas))): print(f"{i+1} - {frutas[i]}")


print("\n\n")