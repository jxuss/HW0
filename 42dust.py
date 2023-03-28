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

import mcb185
import math
import sys

DNA_BASES = 'ACGT'

def calculate_entropy(sequence):
	"""Calculate Shannon entropy of the given DNA sequence."""
	entropy = 0
	for base in DNA_BASES:
		frequency = sequence.count(base) / len(sequence)
		if frequency != 0:
			entropy -= frequency * math.log2(frequency)
	return entropy


for name, sequence in mcb185.read_fasta(sys.argv[1]):

	window_size = int(sys.argv[2])
	threshold = float(sys.argv[3])

	window = sequence[:window_size]
	replacements = 0

	for i in range(len(sequence) - window_size):

		if calculate_entropy(window) < threshold:

			sequence = sequence[:i] + 'N' + sequence[i + 1:]
			replacements += 1

			if replacements % 60 == 0:
				print(sequence[replacements - 60:replacements])

		window = window[1:] + sequence[i + window_size]

	remaining_bases = len(sequence) % 60
	if remaining_bases != 0:
		print(sequence[-remaining_bases:])	

   

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
