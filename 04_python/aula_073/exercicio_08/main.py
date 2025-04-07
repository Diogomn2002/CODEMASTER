print("\n\n")

print("=== Início ===\n")

resposta_1 = input("- Tenho mais de 18 anos? ")

print()

if(resposta_1.lower() == "sim"):
  resposta_2 = input("- Tens carta de condução? ")
  print()
  if(resposta_2.lower() == "nao"): print("Tirar carta")
  print("Dirigir")

else: print("Esperar Crescer")

print("\n\n")