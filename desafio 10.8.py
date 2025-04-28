r1 = int(input('Digite a primeira medida:'))
r2 = int(input('Digite a segunda medida:'))
r3 = int(input('Digite a terceira medida:'))
if r1 <r2+r3 and r2< r1+r3 and r3< r1+r2:
    print('Suas medidas podem ser um triângulo')
   
    if r1== r2 == r3:
        print('Seu triângulo é um triângulo equilátero')
   
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Seu triângulo é um triângulo escaleno')
   
    else:
        print('Seu triângulo é um triângulo isóceles')
else:
    print('Suas medidas não podem ser um triângulo')
