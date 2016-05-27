def somar_pares(lista):
    
    soma = 0
    
    for num in lista:
        if num % 2 == 0:
            soma = soma + num
    return soma
            
            
lista = [10, 5, 7, 9, 20, 2]
result = somar_pares(lista)
print(result)