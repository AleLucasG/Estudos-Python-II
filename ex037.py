"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um numero inteiro: '))
print('ESCOLHA 1 DAS 3 OPÇÕES ABAIXO:')
print('[ 1 ] converte para N° BINÁRIO')
print('[ 2 ] converte para N° OCTAL')
print('[ 3 ] converte para N° HEXADECIMAL')
escolha = int(input('Sua escolha foi: '))

if escolha == 1:
    binario = (bin(num)[2:])
    print('\033[1;33mConvesão do número inteiro {} para BINÁRIO foi de {} \033[m'.format(num, binario))
elif escolha == 2:
    octal = (oct(num)[2:])
    print('\033[1;35mConvesão do número inteiro {} para OCTAL foi de {} \033[m'.format(num, octal))
elif escolha == 3:
    hexagonal = (hex(num)[2:])
    print('\033[1;36mA convesão do número inteiro {} para HEXADECIMAL foi de {}\033[m'.format(num, hexagonal))
