num1 = float(input('Digite seu primeiro número'))
num2 = float(input('Digite seu segundo número'))
num3 = float(input('Digite seu terceiro número'))
#verificando o menor número
if num1<num2 and num1<num3:
    menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#virificando o maior número
if num1>num2 and num1>num3:
    maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
    print('O maior número é o {}'.format(maior))
    print('O menor número é o {}'.format(menor))