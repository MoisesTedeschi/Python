'''
Sequencia de Fibonacci

1,1,2,3,5,8,13,...
'''

def fib(n):
    if n == 0 or n == 1:
        return 1
    
    lista = [1 ,1]
    cont = 2
    
    while cont <= n:
        lista.append(lista[cont-1] + lista[cont-2])
        cont = cont + 1
    
    return lista[n]


termo = 7
print(fib(termo-1))