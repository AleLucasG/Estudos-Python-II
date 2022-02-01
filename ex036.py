"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valorCasa = float(input('Qual valor da casa R$ '))
salario = float(input('Qual o valor do salario do comprador R$ '))
parcelasAnos = int(input('Deseja pagar em quantos anos: '))

teto = salario * 30 / 100

parcelasMeses = parcelasAnos * 12

prestacao = valorCasa / parcelasMeses

if prestacao <= teto:
    print('\033[1;34mEMPRESTIMO LIBERADO!')
    print('Em {} anos, você vai pagar {} parcelas de R$ {:.2f} \033[m'.format(parcelasAnos, parcelasMeses, prestacao))
else:
    print('\033[1;31mEMPRESTIMO NEGADO! \033[m')
