from funcoes import *

limpa()

produtos = ['uva', 'maçã', 'morango', 'ananás', 'banana']

# loop = 0
# while(loop <= 5):
#   print(produtos[loop])
#   loop += 1

print()
print("="*20)
print()

for i in range(len(produtos)): print(f"{i+1} - {produtos[i]}")

print()
print("="*20)
print()

for p in produtos: print(p)

print()
print("="*20)
print()

for p in reversed(produtos): print(p)

print()
print("="*20)
print()

for i in range(len(produtos)-1, -1, -1): print(f"{i+1} - {produtos[i]}")

print("\n\n")