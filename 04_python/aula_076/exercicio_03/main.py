print("\n\n")

# Funções
def converter_para_kelvin():
  resultado = temperatura + 273.15
  print(f"--- ({temperatura:.2f} c) = ({resultado:.2f} k) ---")

def converter_para_far():
  resultado = temperatura * 1.8 + 32
  print(f"--- ({temperatura:.2f} c) = ({resultado:.2f} f) ---")


# Executar
temperatura = float(input("- Digite uma temperatura em celsius: "))
print()
opcao = input("- Você deseja converter para (K)elvin ou (F)ahrenheit? ")
print()

if(opcao.lower() == "k"): converter_para_kelvin()
elif(opcao.lower() == "f"): converter_para_far()
else: print("--- OPÇÃO INVÁLIDA! ---")

print("\n\n")