altura = float(input('Qual a sua altura?:'))
peso = float(input('Qual o seu peso?'))
imc = peso/altura
if imc<18.5:
    print('Você está abaixo do peso recomendado')
elif imc>18.5 and imc<=25:
    print('Parabéns você está no peso ideal')
elif imc>25 and imc<=30:
    print('Você está com sobrepeso, recomendo que procure um médico')
elif imc>30 and imc<=40:
    print('Você está obeso(a),recomendo que procuré um médico e faça exercícios fisicos')
elif imc>40:
    print('CUIDADO, Você atingiu a obesidade mórbida')   