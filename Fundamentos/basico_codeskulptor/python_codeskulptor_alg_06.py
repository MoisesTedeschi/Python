'''
lista = [10, 5, 20]
print(lista[1])
lista[1] = 200
print(lista[1])
'''

tupla = (10, 5, 20)
lista = list(tupla)
lista[1] = 200
tupla = tuple(lista)
print(tupla)