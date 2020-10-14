#   Desafio 066 - Referente aula 15
#   Crie um progrma que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999,
#   que é a condição de parada. No final, mostre quantos números foram digitados
#   e qual foi a soma entre eles (desconsiderando o flag)

# Versão 01

numero = soma = 0

while numero != 999:
    numero = int(input('Digite um valor (999 para parar): '))
    soma += numero

soma -= 999
print(f'A soma dos valores foi {soma}!')


