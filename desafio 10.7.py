salario = float(input('Qual o seu salário?'))
if salario>1250.00:
    preço = (salario* 0.10) + 1250.00
print('Seu novo salário é de exatamente {:.2f}'.format(preço))

if salario<1250.00:
    preço = (salario* 0.15) + 1250.00
    print('Seu novo salário é de exatamente {:.2f}'.format(preço))

    

