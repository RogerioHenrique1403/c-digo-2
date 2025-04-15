name = input('Qual o seu Nome Completo?').strip()
print('voçê possui um total de {} letras'.format(len(name)-name.count(' ')))
print(' Voçê possui um total de {} letras sem espaço'.format(len(name.replace(" ", ""))))
print(name.upper())
print('seu nome primeiro tem {} letras '.format(name.index(' ')))









