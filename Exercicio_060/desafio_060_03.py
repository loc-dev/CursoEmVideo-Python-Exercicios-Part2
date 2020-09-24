#   Desafio 060 - Referente aula Fase14
#   Faça um programa que leia um número qualquer
#   e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#   Versão 03

n = int(input('Qual é o fatorial ?\nDigite um número: '))
print('{}! ='.format(n), end=' ')
f = 1

for i in range(n, 0, -1):
    if i > 1:
        print(i, end=' x ')
    else:
        print(i, end=' = ')
    f *= i

print('{}'.format(f))
