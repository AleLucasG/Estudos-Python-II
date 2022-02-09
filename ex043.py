"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('Seu IMC é de {:.1f}. Você esta Abaixo do peso'.format(imc))
elif 18.6 <= imc <= 24.9:
    print('Seu IMC é de {:.1f}. Você esta no Peso Ideal'.format(imc))
elif 25 <= imc <= 29.9:
    print('Seu IMC é de {:.1f}. Você esta com Sopreso'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é de {:.1f}. Você esta com Obesidade'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Você esta com Odesidade Mórbida'.format(imc))
