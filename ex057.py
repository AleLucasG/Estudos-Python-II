"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peço
a digitação novamente até ter um valor correto"""

sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, qual o seu sexo: ')).strip().upper()[0]
    if sexo == 'F':
        print('Sexo Feminino')
    elif sexo == 'M':
        print('Sexo Masculino')
print('Sexo {} registrado com sucesso'.format(sexo))
