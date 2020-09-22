#   Desafio 057 - Referente aula Fase14
#   Faça um programa que leia o sexo de uma pessoa, mas, só aceite os valores "M" ou "F".
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = "none"

while "M" != sexo != "F":
    sexo = str(input('Informe o seu sexo [ M / F ]: ')).strip().upper()

    if sexo in 'MF':
        print()
        print('Sexo {} registrado com sucesso'.format(sexo))
    else:
        print('Dados inválidos.')
        print()
