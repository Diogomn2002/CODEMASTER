# Importações


# Variáveis
nome = "Harry Potter"
ano = 2002
n_paginas = 412
preco = 32.65

# Executar
print("\n\n")

print("Nome: ({}) | Ano: ({}) | Nº Páginas ({}) | Preço: ({})".format(nome, ano, n_paginas, preco))

print("\n")

print("{3} | {1} | {0} | {2}".format(nome, ano, n_paginas, preco))

print("\n")

print(f"{nome} | {preco} | {n_paginas} | {ano}")

print("\n")

print(f"({nome:>25})")
print(f"({nome:<25})")
print(f"({nome:^25})")

print("\n")

print(f"Preço{preco:.>25}")
print(f"Preço{preco:.<25}")
print(f"Preço{preco:.^25}")

print("\n")

print(f"Preço ({preco:.2f} €)")

print("\n\n")