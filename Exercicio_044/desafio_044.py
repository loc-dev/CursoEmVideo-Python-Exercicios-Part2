#   Desafio 044 - Referente aula Fase12
#   Elabore um programa que calcule o valor a ser pago por um produto,
#   considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque : 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS TOP '))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))

if op == 1:
    total = preco - ((preco * 10) / 100)
elif op == 2:
    total = preco - ((preco * 5) / 100)
elif op == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif op == 4:
    total = preco + ((preco * 20) / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
