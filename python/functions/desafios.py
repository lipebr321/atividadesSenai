#crie uma função que calcule a area de um terreno
print ('Realize aqui seu calculo de area do terreno-->')

def area (n1, n2):
   calculo = n1 * n2
   return calculo

resultado = area(float(input('Digite o comprimento-->  ')), float(input('Digite a largura -->  ')))
print(resultado, 'metros quadrados')

