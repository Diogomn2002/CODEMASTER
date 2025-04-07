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
print("1 - Calcular o Dobro.")
print("2 - Calcular potência.")
print("3 - Cancelar.\n")

opcao = int(input("- Opção: "))

print()

if(opcao == 1): calcular_dobro()
elif(opcao == 2): calcular_potencia()
elif(opcao == 3): print("--- OPERAÇÃO CANCELADA! ---")
else: print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")