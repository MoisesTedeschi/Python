#!/usr/bin/python3

#Passagem de parametro dentro de uma função.
def main():
    verificapar(5)
    verificapar(3)
    verificapar()

#Range é um intervalo de um valor até 10
    
def verificapar(inicio = 1):
    for i in range(inicio, 10):
        print(i, end = ' ')
    print()
    
if __name__ == "__main__" : main()
