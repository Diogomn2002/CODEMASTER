print("\n\n")

# Funções
def calcular_dobro(numero):
  dobro = numero * 2
  print(f"O dobro de ({numero}) é ({dobro})\n")

def calcular_potencia(base, expoente):
  resutaldo = base ** expoente
  print(f"O número ({base}) elevado a ({expoente}) é igual a ({resutaldo})\n")


# Executar
calcular_dobro(2)
calcular_dobro(5)
calcular_dobro(-32)
calcular_dobro(int(input("- Digite um número inteiro: ")))
print("#" * 20)
calcular_potencia(3, 3)
calcular_potencia(-4, 5)
calcular_potencia(11, 2)

print("\n\n")