"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    n = int(input('Quer vera tabuada de qual valor?: '))
    if n < 0:
        break
    print('-' * 30)
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')
    print('-' * 30)
print('Programa finalizado.')
