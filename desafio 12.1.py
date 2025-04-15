casa = int(input('Qual foi o valor da sua casa?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Quantos voçê pretende pagar?'))
prestação = casa/anos
if prestação< salario/0.30:
    print('Seu empréstimo foi aprovado')
else:
    print('Seu empréstimo não foi aprovado')
