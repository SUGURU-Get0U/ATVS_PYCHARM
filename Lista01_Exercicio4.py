#  Escrever um algoritmo para calcular a média de 4 notas.

Nota1 = int(input("Digite a nota 1: "))
Nota2 = int(input("Digite a nota 2: "))
Nota3 = int(input("Digite a nota 3: "))
Nota4 = int(input("Digite a nota 4: "))

PesoNota1 = float(input("Digite o peso da nota 1: "))
PesoNota2 = float(input("Digite o peso da nota 2: "))
PesoNota3= float(input("Digite o peso da nota 3: "))
PesoNota4 = float(input("Digite o peso da nota 4: "))


MediaPonderada = (Nota1 * PesoNota1) + (Nota2 * PesoNota2) + (Nota3 * PesoNota3) + Nota4 * PesoNota4
MediaPonderada2 = MediaPonderada / (PesoNota4 + PesoNota3 + PesoNota2 + PesoNota1)

Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4

print(f"A media das quatro notas é de: {Media:.1f}")
print(f"A media ponderada das 4 notas é de: {MediaPonderada2:.2f}")

if Media or MediaPonderada2 >= 7:
    print("o Aluno está aprovado")

elif Media or MediaPonderada2 >= 4:
    print("O aluno está de recuperação")

else:
    print("o Aluno está reprovado")
