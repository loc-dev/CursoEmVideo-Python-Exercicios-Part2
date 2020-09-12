#   Desafio 053 - Referente aula Fase13
#   Crie um programa que leia uma frase qualquer
#   e diga se ela é um palíndromo, desconsiderando os espaços.

#   Exemplos:
#   APOS A SOPA
#   A SACADA DA CASA
#   A TORRE DA DERROTA
#   O LOBO AMA O BOLO
#   ANOTARAM A DATA DA MARATONA

#   Versão 02

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
