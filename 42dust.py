# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)
# cd ~/Code/HWnow 
# python3 42dust.py test.fa 11 1.4

import sys
import mcb185
import math

file = sys.argv[1]
window = int(sys.argv[2])
threshold = float(sys.argv[3])

def entropy(seq):
	ea = 0
	et = 0
	ec = 0
	eg = 0
	for nt in seq:
		if nt == 'A': ea += 1
		elif nt == 'T': et += 1
		elif nt == 'C': ec += 1
		elif nt == 'G': eg += 1
	prob = [ea/len(seq), et/len(seq), ec/len(seq), eg/len(seq)]
	h = 0
	for p in prob:
		if p == 0: continue
		h -= p*math.log2(p)
	return h

seqs = []
for defline, seq in mcb185.read_fasta(file):
	seq = seq.upper()
	new_seq = ''
	for i in range(0, len(seq)):

		if entropy(seq[i:i+window]) < threshold:
			new_seq += 'N'
		else:
			new_seq += seq[i]
	seqs.append((defline, new_seq))

for defline, seq in seqs:
	print(f'>{defline}')
	for i in range (0, len(seq),60):
		print(seq[i:i+60])
		

   

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
python3 42dust.py test.fa 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
