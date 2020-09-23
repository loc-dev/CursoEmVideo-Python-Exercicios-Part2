#   Desafio 059 - Referente aula Fase14
#   Crie um programa que leia dois valores
#   e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso.

#   [ 1 ] Somar
#   [ 2 ] Multiplicar
#   [ 3 ] Maior
#   [ 4 ] Novos números
#   [ 5 ] Sair do programa

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0

while op != 5:

    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    op = int(input('>>>> Qual é a sua opção? '))

    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        prod = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, prod))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente Novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
