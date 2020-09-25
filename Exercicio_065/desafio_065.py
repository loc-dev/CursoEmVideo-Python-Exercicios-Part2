#   Desafio 065 - Referente aula Fase14
#   Crie um programa que leia vários números inteiros pelo teclado.
#   No final da execução, mostre a média entre todos os valores e qual foi
#   o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
#   ou não continuar a digitar valores.

resp = 'S'
s = q = m = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    q += 1

    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

m = s / q
print('Você digitou {} números e a média foi {}'.format(q, m))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
