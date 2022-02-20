"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

"""num = [0,1,2,3,4,5,6,7,8,9,10]
computador = choice(num)
num = int(input('Qual número você escolheu: '))
print('O computador escolheu o número: {}'.format(computador))
if num == computador:
    print('\033[1;35mMEUS PARABÉNS, VOCÊ ACERTOU! \033[m')
else:
    print('\033[1;36mMELHOR SORTE NA PROXIMA TENTATIVA! \033[m')"""


from random import randint

computador = randint(0, 10)
print('\033[1;32mSou seu computador... Acabei de pensar em um númeri entre 0 e 10')
print('Será que você consegue adivinha o número? \033[m')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual seu palpite: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vex.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Meus Parabens!'.format(palpites))

