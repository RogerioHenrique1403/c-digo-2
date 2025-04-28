ano = int(input('Digite seu ano de nascimento:'))
calculo = 2025-ano
if calculo<18:
    print('você ainda vai poder se alistar')
elif calculo==18:
    print('já é hora de você se alistar')
elif calculo>18:
    print('Já passou da hora de você se alistar ')