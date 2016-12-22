'''
Algoritmo vai receber uma sequência de DNA
e vai gerar a contagem de nucleotídeos. 
'''

#Variável recebe a sequência
seq = "aCC CCT ATG TGACCA ctG"

#O método upper transforma as letras minúsculas em
#maiúsculas
seq = seq.upper()

#Elimina os espaços que estão dentro da sequência de DNA
seq = seq.replace(' ', '')

print("Sequência informada:", seq)
print("A Quantidade de Adenina é:", seq.count('A'))
print("A Quantidade de Timina é:", seq.count('T'))
print("A Quantidade de Citosina é:", seq.count('C'))
print("A Quantidade de Guanina é:", seq.count('G'))