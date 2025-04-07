print("\n\n")

# Funções
def saudar():
  print("-"*20)
  print("Boa noite Codemaster")
  print("-"*20)

def saudar_2(nome):
  print("-"*20)
  print(f"Boa noite {nome}")
  print("-"*20)

def calcular_desconto(preco, percentagem):
  novo_preco = preco * (100 - percentagem) / 100
  print("-"*20)
  print(f"O preço ( {preco:.2f} € ) com um desconto de ({ percentagem:.1f} % ) vai dar ( {novo_preco:.2f} € )")
  print("-"*20)

# Executar
saudar()
saudar()
saudar()

print("#"*20)

x = "José"

saudar_2("fabricio")
saudar_2("maria")
saudar_2("joao")
saudar_2(x)

print("#"*20)

calcular_desconto(100, 5)
calcular_desconto(33.54, 12.5)
calcular_desconto(1234.50, 3)


print("\n\n")