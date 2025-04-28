ano = int(input('Qual ano de nascimento?:'))
calculo = 2025-ano
if calculo<=9:
    print('Mirim')
elif calculo>9 and calculo<=14:
    print('Infantil')
elif calculo>14 and calculo<=19:
    print('Junior')
elif calculo>19 and calculo==20:
    print('Sênior')
elif calculo>20:
    print('Master')
    

