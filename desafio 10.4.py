km = float(input('Qual a distância da sua viagem?'))
if km<= 200:
    preço = km*0.50
else:
    preço = km*0.45
    print('O preço da sua passagem é de exatamente {:.2f} Reais'.format(preço))

 
