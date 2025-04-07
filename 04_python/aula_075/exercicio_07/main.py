print("\n\n")

# Funções
def calcular_dobro():
  numero = int(input("- Digite um número inteiro: "))
  dobro = numero * 2
  print(f"\nO dobro de ({numero}) é ({dobro})\n")

def calcular_potencia():
  base = float(input("- Digite o valor da base: "))
  expoente = float(input("- Digite o valor do expoente: "))
  resutaldo = base ** expoente
  print(f"\nO número ({base}) elevado a ({expoente}) é igual a ({resutaldo})\n")

# Executar
print("=== Menu da Aplicação ===\n")
print("A - Calcular o Dobro.")
print("B - Calcular potência.")
print("C - Cancelar.\n")

opcao = input("- Opção: ")

print()

if(opcao.lower() == "a"): calcular_dobro()
elif(opcao.lower() == "b"): calcular_potencia()
elif(opcao.lower() == "c"): print("--- OPERAÇÃO CANCELADA! ---")
else: print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")