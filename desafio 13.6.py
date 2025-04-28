Termo = int(input('Digite o primeiro termo da PA: '))
Razao = int(input('Digite a razão da PA: '))
formula = Termo + (10-1) * Razao
for c in range(Termo, formula+Razao, Razao):
    print(c)