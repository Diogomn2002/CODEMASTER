print("\n\n")

# Funções
def converter_para_kelvin():
  c = float(input("- Digite uma temperatura em celsius: "))
  resultado = c + 273.15
  print(f"\n--- ({c:.2f} c) = ({resultado:.2f} k) ---")

def converter_para_far():
  c = float(input("- Digite uma temperatura em celsius: "))
  resultado = c * 1.8 + 32
  print(f"\n--- ({c:.2f} c) = ({resultado:.2f} f) ---")


# Executar
opcao = input("- Você deseja converter para (K)elvin ou (F)ahrenheit? ")

print()

if(opcao.lower() == "k"): converter_para_kelvin()
elif(opcao.lower() == "f"): converter_para_far()
else: print("--- OPÇÃO INVÁLIDA! ---")


print("\n\n")