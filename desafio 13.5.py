soma = 0
cont = 0
for c in range (1,7):
    número = int(input('Digite seu número:'))
    if c % 2 == 0:
            cont =cont +1
            soma+=número 
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
    