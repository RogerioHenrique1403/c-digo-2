import random
itens = ('pedra', 'papel', 'tesoura')
pc = random.randint(0, 2)
print('''ESCOLHA SUA OPÇÃO
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opções = int(input('Qual a sua escolha?:'))
print('Computador escolheu {}'.format(itens[pc]))
print('Voçê escolheu {}'.format(itens[opções]))
if pc== 0:
    if opções == 0:
        print('EMPATE')
    elif opções == 1:
        print('VOCÊ GANHOU')
    elif opções == 2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc== 1:
    if opções == 1:
        print('EMPATE')
    elif opções == 2:
        print('VOCÊ GANHOU')
    elif opções == 3:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc== 2:
    if opções == 2:
        print('EMPATE')
    elif opções == 0:
        print('VOCÊ GANHOU')
    elif opções == 1:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')

