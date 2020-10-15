#   Desafio 070 - Referente aula 15
#   Crie um programa que leia o nome e o preço de vários produtos.
#   O programa deverá perguntar se o usuário vai continuar.
#   No final, mostre:

#   A) Qual é o total gasto na compra.
#   B) Quantos produtos custam mais de R$1000.00.
#   C) Qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1
    
    # Total da compra
    total += preco

    # Produtos custam mais de R$ 1000.00
    if preco > 1000:
        totmil += 1

    # Verificação do nome do produto com menor preço
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S | N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
