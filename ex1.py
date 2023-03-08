# Exercício 1 = Ordenando valores pares e ímpares

from random import randint
lista = []
impar = []
par = []

for i in range(20):
  lista.append(int(input(" ")))
  if lista[i] % 2 == 0:
    par.append(lista[i])
  else:
    impar.append(lista[i])

print(lista)
print(par)
print(impar)
