produto = float(input('Qual vai ser o valor a ser pago?'))
print('''Pagamentos disponíveis?
[1] Dinheiro
[2] Cartão
[3] Cartão2x
[4] Cartão3x
[5] Cartão4x
[6] Cartão5x
[7] Cartão6x
[8] Cartão7x
[9] Cartão8x
[10] Cartão9x
[11] Cartão10x
[12] Cartão11x
[13] Cartão12x''')
opção = int(input('Qual forma de pagamento?:'))
din = produto-(produto*0.10)
cart = produto-(produto*0.05)
cart2x = produto/2
cart4x = (produto * 1.20) / 4
cart5x = (produto * 1.20) / 5
cart6x = (produto * 1.20) / 6
cart7x = (produto * 1.20) / 7
cart8x = (produto * 1.20) / 8
cart9x = (produto * 1.20) / 9
cart10x = (produto * 1.20) / 10
cart11x = (produto * 1.20) / 11
cart12x = (produto * 1.20) / 12

if opção == 1:
    print('Pague {:.2f} Reais'.format(din))
elif opção == 2:
        print('Pague {:.2f} Reais'.format(cart))
elif opção == 3:   
        print('Pague {:.2f} Reais'.format(cart2x)) 
elif opção == 4:   
        print('Pague {:.2f} Reais'.format(cart3x))
elif opção == 5:
    print('Pague {:.2f} Reais'.format(cart4x))
elif opção == 6:
     print('Pague {:.2f} Reais'.format(cart5x))
elif opção == 7:
      print('Pague {:.2f} Reais'.format(cart6x))
elif opção == 8:
      print('Pague {:.2f} Reais'.format(cart7x))
elif opção == 9:
      print('Pague {:.2f} Reais'.format(cart8x))
elif opção == 10:
      print('Pague {:.2f} Reais'.format(cart9x))
elif opção == 11:
      print('Pague {:.2f} Reais'.format(cart10x))
elif opção == 12:
      print('Pague {:.2f} Reais'.format(cart11x))
elif opção == 13:
      print('Pague {:.2f} Reais'.format(cart12x))