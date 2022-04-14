def euclides(a, b):
  while (b != 0):
    r = a % b
    a = b
    b = r
  return a
  
if __name__ == '__main__':
  a = int(input('Digite o primeiro número: '))
  b = int(input('Digite o segundo número: '))

  print(euclides(a, b))