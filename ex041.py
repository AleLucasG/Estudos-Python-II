"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date

ano = int(input('Qual seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano

if idade <= 9:
    print('{} ANOS - CATEGORIA MIRIM'.format(idade))
elif idade <= 14:
    print('{} ANOS - CATEGORIA INFNTIL'.format(idade))
elif idade <= 19:
    print('{} ANOS - CATEGORIA JÚNIOR'.format(idade))
elif idade <= 25:
    print('{} ANOS - CATEGORIA SÊNIOR'.format(idade))
else:
    print('{} ANOS - CATEGORIA MASTER'.format(idade))
