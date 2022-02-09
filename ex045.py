"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)

print('\033[1;36m===== VAMOS JOGAR JO KEN PÔ ===== \033[m')
print('\033[1;36m===== Escolha sua jogada ===== \033[m')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
usuario = int(input('Qual sua escolha: '))

print('\033[1;33m=== JO === \033[m')
sleep(1)
print('\033[1;33m==== KEN ====\033[m')
sleep(1)
print('\033[1;33m===== PÔ! ===== \033[m')
sleep(1)

print('\033[1;36m=\033[m' * 30)
print('Computador escolheu: \033[1;33m{} \033[m'.format(itens[computador]))
print('Você escolheu: \033[1;33m{} \033[m'.format(itens[usuario]))
print('\033[1;36m=\033[m' * 30)

if computador == 0:
    if usuario == 0:
        print('\033[1;33mDEU EMPATE! \033[m')
    elif usuario == 1:
        print('\033[1;32mVOCÊ VENCEU! \033[m')
    elif usuario == 2:
        print('\033[1;31mCOMPUTADOR VENCEU \033[m')
    else:
        print('\033[1;37mJOGADA INVALIDA \033[m')
elif computador == 1:
    if usuario == 0:
        print('\033[1;31mCOMPUTADOR VENCEU \033[m')
    elif usuario == 1:
        print('\033[1;33mDEU EMPATE! \033[m')
    elif usuario == 2:
        print('\033[1;32mVOCÊ VENCEU! \033[m')
    else:
        print('\033[1;37mJOGADA INVALIDA \033[m')
elif computador == 2:
    if usuario == 0:
        print('\033[1;32mVOCÊ VENCEU! \033[m')
    elif usuario == 1:
        print('\033[1;31mCOMPUTADOR VENCEU \033[m')
    elif usuario == 2:
        print('\033[1;33mDEU EMPATE! \033[m')
    else:
        print('\033[1;37mJOGADA INVALIDA \033[m')
