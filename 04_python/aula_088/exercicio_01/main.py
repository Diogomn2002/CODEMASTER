from funcoes import *

limpa()

frutas = ["uva", "maça", "morango"]

print(f"Lista original: {frutas}\n")

print("- Adicionar 'ananás'.\n")
frutas.append("ananás")
print(f"Lista modificada: {frutas}\n")

print("- Inserir 'laranja' na segunda posição.\n")
frutas.insert(1, "laranja")
print(f"Lista modificada: {frutas}\n")

print("- Remover o primeiro elemento.\n")
frutas.pop(0)
print(f"Lista modificada: {frutas}\n")

print("- Remover o 'morango'.\n")
frutas.remove("morango")
print(f"Lista modificada: {frutas}\n")

print("\n\n")