Ex3 - Mostra o atleta, os seus saltos e a média entre todos eles

atleta = input("Digite o nome do atleta: ")
salto = []
while atleta != "0":
  for i in range(5):
    salto.append(float(input("Salto: ")))
  print("")
  print(f"Atleta: {atleta}")
  print("")
  print(f"Primeiro salto: {salto[0]} m")
  print(f"Segundo salto: {salto[1]} m")
  print(f"Terceiro salto: {salto[2]} m")
  print(f"Quarto salto: {salto[3]} m")
  print(f"Quinto salto: {salto[4]} m")
  print("")
  print("Resultado final:")
  print("")
  print(atleta)
  print(f"Saltos: {salto[0]} - {salto[1]} - {salto[2]} - {salto[3]} - {salto[4]}")
  media = sum(salto) / 5
  salto = []
  print("Média: {} m" .format(round(media, 2)))
  
  atleta = input("\nDigite o nome do atleta: ")
  if atleta != "0":
    continue
