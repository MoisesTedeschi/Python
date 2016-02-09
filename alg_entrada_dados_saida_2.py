"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)
 
EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>> 
"""
x = 15
y = 10
print("A Soma entre x e y:",x,"+",y,"=",x + y)
print("A Subtração entre x e y:",x,"-",y,"=",x - y)
print("A Multiplicação entre x e y:",x,"*", y,"=",x * y)
print("A Divisão entre x e y:",x,"/", y,"=",x / y)
print("A Divisão Inteira entre x e y:",x,"//", y,"=",x // y)
print("O Resto da Divisão entre x e y:",x,"resto",y,"=",x % y)
print("A potencia entre x e y: ",x,"potencia", y,"=",x ** y)



