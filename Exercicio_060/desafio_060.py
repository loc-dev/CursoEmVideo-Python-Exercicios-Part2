#   Desafio 060 - Referente aula Fase14
#   Faça um programa que leia um número qualquer
#   e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)

print('O fatorial de {} é {}.'.format(n, f))
