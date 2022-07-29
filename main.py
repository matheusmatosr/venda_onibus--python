def geraMatriz():
  matriz =  [[0]*3 for _ in range(16)]
  return matriz

def exibeMatriz(matriz):
  for linha in matriz:
    for coluna in linha:
      print(coluna, end=' | ')
    print()

# letra A
def venda(matriz):
  continuar = 's'
  while continuar == 's':
    idade = int(input('Idade: '))
    fileira = int(input('Fileira: ')) - 1
    poltrona = int(input('Poltrona: ')) - 1
    if matriz[fileira][poltrona] == 0:
      matriz[fileira][poltrona] = idade
    else:
      print('Assento ocupado!')
    continuar = input('Deseja continuar? ')
  return matriz

# letra B
def assentos(matriz):
  soma = 0
  soma2 = 0
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] == 0:
        soma = soma + 1
      else:
        soma2 = soma2 + 1
  print(f'Assentos livres: {soma}')
  print(f'Assentos ocupados: {soma2}')

# letra C
def faixa(matriz):
  cont = 0
  soma = 0
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] != 0:
        cont =  cont + 1
        soma = soma + matriz[l][c]
  media = soma/cont
  print(f'Faixa etária: {media}')

# letra D
def arrecadado(matriz):
  total = 0
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] !=  0:
        if c == 1:
          if matriz[l][c] <= 12:
            total = total + 100
          elif matriz[l][c] >= 13 and matriz[l][c] <= 18:
            total = total + 200
          elif matriz[l][c] >= 19:
            total = total + 300
        else:
          if matriz[l][c] <= 12:
            total = total + 150
          elif matriz[l][c] >= 13 and matriz[l][c] <= 18:
            total = total + 260
          elif matriz[l][c] >= 19:
            total = total + 370
  print(f'Total arrecadado: {total}')

# letra E
def maior(matriz):
  maior = matriz[0][0]
  for i in matriz:
    for valor in i:
      if valor > maior:
        maior = valor
  print(f'Maior idade cadastrada: {maior}') 

def main():
  m = geraMatriz()
  v = venda(m)
  a = assentos(m)
  f = faixa(m)
  ar = arrecadado(m)
  ma = maior(m)
  e = exibeMatriz(m)

main()