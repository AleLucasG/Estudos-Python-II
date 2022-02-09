"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele:
- ainda vai se alistar ao serviço militar,
- se é a hora exata de se alistar ou,
- se já passou do tempo do alistamento.
- Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

ano = int(input('Qual ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 17:
    print('\033[1;33mVocê ainda não tem idade para se alistar no exercito.')
    falta = 18 - idade
    print('Faltam {} anos para você se alistar. \033[m'.format(falta))
elif idade == 18:
    print('\033[1;32mMEUS PARABÉNS!! Você já tem {} anos e já pode se alistar no exercito! \033[m'.format(idade))
else:
    print('\033[1;31mInfelismente já passou do tempo do alistamento! \033[m')
