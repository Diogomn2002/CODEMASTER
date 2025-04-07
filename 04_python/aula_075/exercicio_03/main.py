print("\n\n")

# Funções
def calcular_area_triangulo():
  base = float(input("- Digite o valor da base do triângulo: "))
  altura = float(input("- Digite o valor da altura do triângulo: "))
  area = base * altura / 2
  print(f"A área deste triângulo é de ( {area:.1f} )")

def calcular_area_rectangulo():
  base = float(input("- Digite o valor da base do rectângulo: "))
  altura = float(input("- Digite o valor da altura do rectângulo: "))
  area = base * altura
  print(f"A área deste rectângulo é de ( {area:.1f} )")


# Executar
calcular_area_triangulo()
print("#"*20)
calcular_area_rectangulo()


print("\n\n")