#!usr/bin/python3
def main():

    x = input("Entre com o primeiro valor: ")
    y = input("Entre com o segundo valor: ")

    if x < y:
        print("O X: ",x," é menor que Y: ",y)
    elif x == y:
        print("Os valores de entrada são iguais!")
    else:
        print("O X:",x," não é maior que Y: ",y)

    
    print("Rodando a função main()!")

if __name__ == "__main__" : main()

