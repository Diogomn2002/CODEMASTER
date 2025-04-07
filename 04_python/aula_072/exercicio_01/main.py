print("\n\n")


print("\n=== Média Escolar ===")

print("\n")

nome = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a nota da prova 1: "))
nota_2 = float(input("Digite a nota da prova 2: "))
trabalho_casa = float(input("Digite a nota do trabalho de casa: "))

media = (nota_1 + nota_2 + trabalho_casa) / 3

print("\n")

print(f"O(a) aluno(a) {nome} obteve uma média final de ({media:.1f}) valores.")

print("\n\n")
