'''
Efetuando a tradução de uma sequência de RNA para
Proteína.
'''
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

'''
Entrando com uma sequência de DNA. A sequência precisa ser um multiplo de 3.
Codons são compostos por 3 bases de nucleotídeos. Cada Codon representa uma trilpa.
Ou seja, um aminoácido. 
'''
seq_dna = Seq("ATCGATTGCCGCGTTCGA", IUPAC.unambiguous_dna)
#Transformando a sequência de DNA em uma de RNA.
seq_rna = seq_dna.transcribe()

#Traduzindo a sequencia do RNA em uma proteína.
nova_proteina = seq_rna.translate()

print("Nova proteína gerada: %s" % nova_proteina)

#A sequência de DNA pode ser diretamente traduzida para uma proteína.
print("Exibindo uma tradução de DNA para Proteínas:",seq_dna.translate())