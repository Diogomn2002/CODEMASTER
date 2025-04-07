print("\n\n")

# Funções
def converter_para_kelvin(c):
  resultado = c + 273.15
  print(f"--- ({c:.2f} c) = ({resultado:.2f} k) ---")

def converter_para_far(c):
  resultado = c * 1.8 + 32
  print(f"--- ({c:.2f} c) = ({resultado:.2f} f) ---")

# Executar
temperatura = float(input("- Digite uma temperatura em celsius: "))
print()
opcao = input("- Você deseja converter para (K)elvin ou (F)ahrenheit? ")
print()

if(opcao.lower() == "k"): converter_para_kelvin(temperatura)
elif(opcao.lower() == "f"): converter_para_far(temperatura)
else: print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")