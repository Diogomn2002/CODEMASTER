import os
import time

# Funções

print("\n==== Escola Codemaster ====\n ")

alunos = float(input("-Digite o total de alunos da turma: "))

total_idades = 0
loop = 1

while loop <= alunos:
  idade = float(input(f"- Digite a idade do(a) [{loop}] aluno(a): "))
  total_idades += idade
  loop += 1

#Média Aritmética
media = total_idades / alunos

#Resultado Final
print(f"A média de idades desta turma é de ({media:.1f} anos)")

print("\nFIM")


# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(segundos): time.sleep(segundos)

def animar(frase, tempo):
  limpa()
  print(frase, end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  limpa()