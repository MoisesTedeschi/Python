'''
Exemplos de numeros primos:

7,11,13,...
'''

def primo(n):
    
    cont_div = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont_div = cont_div + 1
   
    if cont_div <= 2:
        return True
    return False


print(primo(2))