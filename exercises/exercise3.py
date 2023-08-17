import math

print('escolha 2 numeros')

n1 = float(input())
n2 = float(input())

if n1>n2:
    quadrado = math.pow(n1,2)
else:
    quadrado = math.pow(n2,2)
print('o numero maior ao quadrado é: ', quadrado)