soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma= soma+cont
print('O calculo das somas de {} foi de {}'.format(cont, soma))