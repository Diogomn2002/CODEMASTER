print("\n\n")

# Funções
def calcular_antecessor():
  numero = int(input("- Digite um número inteiro: "))
  antecessor = numero - 1
  print(f"O antecessor do número ({numero}) é ({antecessor})")

def calcular_antecessor_2(numero):
  antecessor = numero - 1
  print(f"O antecessor do número ({numero}) é ({antecessor})")

# Executar
calcular_antecessor()
print("#"*20)

# calcular_antecessor_2(int(input("- Digite um número inteiro: ")))

x = int(input("- Digite um número inteiro: "))
calcular_antecessor_2(x)

print("\n\n")