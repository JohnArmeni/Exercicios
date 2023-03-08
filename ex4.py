#Ex4 - uma função que retorna somente os valores de uma lista que se iniciarem e terminarem com o mesmo caractere

def contaCondicional(x):

  listaCondicional = []
  for i in x:
    if i[0] == i[-1]:
      listaCondicional.append(i)

  return len(listaCondicional)


listaOrganizada = ['abc', '1221', 'xyzx', '45634', '3324', 'qwer', '0340']
contaCondicional(listaOrganizada)
