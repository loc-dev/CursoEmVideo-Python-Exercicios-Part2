#   Desafio 039 - Referente aula Fase12
#   Faça um programa que leia o ano de nascimento de um jovem
#   e informe, de acordo com a sua idade, se ele ainda vai se alistar
#   ao serviço militar, se é a hora de se alistar ou se já passou do tempo
#   do alistamento. Seu programa também deverá mostrar o tempo que falta
#   ou que passou de prazo.

#   Versão 2

from datetime import date

ano_atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
sexo = str(input('''Sexo:
[ M ] para Masculino
[ F ] para Feminino
Sua opção: '''))
sexo = sexo.replace(' ', '').upper()
idade = ano_atual - nasc

if sexo == 'M':
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano_atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = ano_atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
        ano = ano_atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 'F':
    print('Você não precisa realizar o alistamento militar obrigatório.')
else:
    print('Opção inválida! Tente novamente')
