"""
Faça um programa para uma loja de tintas.
 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
 
Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""

area = int(input("Entre com a área a ser pintada: "))
litros = area//3
#Se a divisão por 3 for maior que zero soma 1 ao total de litros
if area % 3 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Você precisará de: ",latas,"latas.")
print("Você vai pagar R$ ",latas*80)
