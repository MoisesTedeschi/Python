'''
Dogma da biomolecular:
De DNA para DNA o processo ocorre por Cópia;
De DNA para RNA o processo é por Transcrição;
Do RNA para Proteínas o processo é por tradução.

'''
#Exemplo de um processo de transcrição usando Biopython

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna_base = Seq("ACTGCTCCATAG", IUPAC.unambiguous_dna)
print("DNA informado:", dna_base)

rna_transcrito = dna_base.transcribe()
print("RNA transcrito:", rna_transcrito)