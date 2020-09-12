#   Desafio 056 - Referente aula Fase13
#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#   No final do programa, mostre:

# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

soma_idade = 0
media_idade = 0

maior_idade_homem = 0
nome_homem_maior = ''

total_mulher20 = 0

for pessoa in range(1, 5):
    print('----- {}ª PESSOA-----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_maior = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_maior = nome

    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher20))
