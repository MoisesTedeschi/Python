'''
Criando uma sequência complementar de DNA
e imprimindo a sequência complementar e o reverso
Complementar.
'''
from Bio.Seq import Seq

seq = Seq("ACCCCTATGTGACCACTG")
print("Imprimindo sequência complementar: ", seq.complement())

print("Imprimindo o reverso complementar:", seq.reverse_complement())