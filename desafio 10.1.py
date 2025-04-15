import random
dig = int(input('Qual foi o número pensado?'))
pc = random.randint(0,5)
if pc!=dig:
    print('Infelizmente voçê não acertou tente na proxima')
else:
    print('Voçê adivinhou')