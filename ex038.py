"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
– O primeiro valor é maior;
– O segundo valor é maior;
– Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\033[1;33mO primeiro número digitado foi {} e ele tem valor maior do que {} \033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[1;34mO segundo número digitado foi {} e ele tem valor maior do que {} \033[m'.format(n2, n1))
else:
    print('\033[1;35mNão existe valor maior, os dois são iguais \033[m')
