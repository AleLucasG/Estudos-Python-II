"""Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500."""

soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print('\033[1;34mA soma de todos os {} valores encontraos é: {}\033[m \n'.format(cont, soma))

soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma = soma + num
print('\033[1;35mA soma dos múltiplos de três é: {} \033[m'.format(soma))
