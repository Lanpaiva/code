n1 = int(input('digite um numero'))

respostaPositiva = 'O número é divisível por 3 e 5'
respontaNegativa = 'O número não é divisível por 3 e 5'

if n1 % 3 == 0 and n1 % 5 == 0:
    print(respostaPositiva)
else:
    print(respontaNegativa)