"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

print('===== \033[1;36m MÉDIA ESCOLAR \033[m=====')
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))

media = (nota1 + nota2) / 2
if media >= 7:
    print('\033[1;32mSua média é {}. VOCÊ FOI APROVADO! \033[m'.format(media))
elif 5 >= media <= 6.9:
    print('\033[1;33mSua média é {}. VOCÊ ESTA DE RECUPERAÇÃO \033[m.')
else:
    print('\033[1;31mSua média é {}. VOCÊ FOI REPORVADO! \033[m'.format(media))

