# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import gzip
import re
import sys

from Bio.Seq import Seq

with gzip.open(sys.argv[1], 'rt') as f:

    dna = ''
    for line in f:
        if line.startswith('ORIGIN'):
            for line in f:
                seq = re.sub(r'\d|\s', '', line)
                dna += seq

dna_seq = Seq(dna)

counts = {}
with gzip.open(sys.argv[1], 'rt') as f:
    for line in f:
        if line.startswith('     CDS'):
            m = re.search(r'(\d+)\.\.(\d+)', line)
            if m:
                start, end = int(m.group(1)), int(m.group(2))
                if 'complement' in line:
                    cds = dna_seq[start-1:end].reverse_complement()
                else:
                    cds = dna_seq[start-1:end]
                start_codon = cds[:3]
                counts[start_codon] = counts.get(start_codon, 0) + 1

for codon, count in counts.items():
    print(codon.upper(), count)


"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
