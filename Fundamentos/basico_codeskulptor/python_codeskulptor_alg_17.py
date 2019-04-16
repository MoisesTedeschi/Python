'''
base e expoente

Exemplo:
base = 2
expoente: 3

2^3 = 2 * 2 * 2 = 8
'''

def pot(base, exp):
    
    mult = 1
    for i in range(0,exp):
        mult = mult * base
        
    return mult


print(pot(3,3))