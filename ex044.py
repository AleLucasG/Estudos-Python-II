"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juro"""

produto = float(input('Qual valor do produto R$ '))
print('\033[1;33m=== FORMAS DE PAGAMENTOS === \033[m')

print('[ 1 ] à VISTA/CHEQUE: \033[1;31m10% DE DESCONTO \033[m')
print('[ 2 ] à VISTA NO CARTÃO: \033[1;31m5% DE DESCONTO \033[m')
print('[ 3 ] em ATÉ 2X NO CARTÃO: \033[1;31mSEM DESCONTOS \033[m')
print('[ 4 ] 3X OU MAIS NO CARTÃO: \033[1;31m20% DE JUROS \033[m')
escolha = int(input('Qual a forma de pagamento: '))

if escolha == 1:
    desconto = (produto * 10) / 100
    print('O produto custa R$ {:.2f} reais e teve desconto de 10% de R$ {:.2f} reais.'.format(produto, desconto))
elif escolha == 2:
    desconto = (produto * 5) / 100
    print('O produto custa R$ {:.2f} reais e teve desconto de 5% de R$ {:.2f} reais.'.format(produto, desconto))
elif escolha == 3:
    print('O produto custa R$ {:.2f} reais, sem descontos.'.format(produto))
elif escolha == 4:
    desconto = (produto * 20) / 100
    print('O produto custa R$ {:.2f} reais e teve um acrescimo de juros de R$ {:.2f}.'.format(produto, desconto))
else:
    print('\033[1;31mOPÇÃO ERRADA. POR FAVOR, ESCOLHAS UMA DAS OPÇÕES INFORMADAS. \033[m')

