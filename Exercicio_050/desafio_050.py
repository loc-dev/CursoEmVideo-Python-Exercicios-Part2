#   Desafio 050 - Referente aula Fase13
#   Desenvolva um programa que leia seis números inteiros
#   e mostre a soma apenas daqueles que forem pares.
#   Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for i in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você informou {} número(s) par(es) e a soma foi {}!'.format(cont, soma))
