print('Digite as três notas')

n1 = float(input())
n2 = float(input())
n3 = float(input())

print('Digite o peso de cada nota')

p1 = float(input())
p2 = float(input())
p3 = float(input())

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print('Média ponderada, fazendo multiplicação, e a divisão pela soma dos pesos: ', media)
