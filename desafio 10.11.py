nota1 = float(input('Qual a sua nota?:'))
nota2 = float(input('Qual a sua nota?:'))
média = (nota1+nota2)/2
if média<5.0:
    print('Reprovado')
elif média>5.0 and média<7:
    print('Recuperação')
elif média>=7:
    print('Aprovado')
