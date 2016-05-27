'''
Numero perfeito: eh um numero
onde a soma dos seus divisores
positivos (exceto o proprio
numero) eh igual a esse numero

Exemplo: 6

6 = 1 + 2 + 3 = 6
'''

def perfeito(num):
    
    soma = 0
    for div in range(1,num):
        if num % div == 0:
            soma = soma + div
            
    if soma == num:
        return True
    
    return False


print(perfeito(496))