num = int(input('Digite um número:'))
print('''Escolha uma das opções abaixo
      (1) CONVERTER PARA BINÁRIO
      (2) CONVERTER PARA OCTAL
      (3) CONVERTER PARA HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertito para HEXADECIMAL é igual a {}'.format(num, hex(num)))

