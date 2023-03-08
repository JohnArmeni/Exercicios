# Exercício 2 - Mostra somente as médias que forem iguais ou maior que 7

qtdeAlunos = int(input("Insira a quantidade de alunos que irão participar: "))
qtdeNotas = int(input("Quantas notas para cada aluno?: "))
mediaAlunos = []
for num in range(qtdeAlunos):
  nomeAluno = input("Nome do aluno: ")
  somaNotas = 0

  for num in range(qtdeNotas):
    nota = float(input("Digite as notas: "))
    somaNotas += nota
    
  mediaNotas = somaNotas / qtdeNotas
  mediaAlunos.append(mediaNotas)

for num in mediaAlunos:
  if num >= 7:
    print("Essas foram as maiores medias:")
    print(num, end = " ")
