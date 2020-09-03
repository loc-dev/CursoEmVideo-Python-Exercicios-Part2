#   Desafio 041 - Referente aula Fase12
#   A Confederação Nacional de Natação precisa de um programa que leia,
#   o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.

#   Até 9 anos: Mirim
#   Até 14 anos: Infantil
#   Até 19 anos: Júnior
#   Até 25 anos: Sênior
#   Acima: Master

from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
