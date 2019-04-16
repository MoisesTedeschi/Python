'''
0! = 1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
...
'''

def fatorial(num):
    
    mult = 1
    for i in range(num, 0, -1):
        mult = mult * i
    return mult

print(fatorial(0))