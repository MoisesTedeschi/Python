'''
Recursividade

Quando uma funcao chama a
si propria.
'''

def pot(base, exp):
    
    # caso base
    if exp == 0:
        return 1  
    
    return base * pot(base, exp-1)

print(pot(3,4))