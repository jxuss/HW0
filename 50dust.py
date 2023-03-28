# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)
# cd ~/Code/HWnow 
# python3 50dust.py -w 11 -t 1.4 -s test.fa  | head

import argparse
import math
import mcb185

parser = argparse.ArgumentParser(description='Entropy')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('-w', required=False, type=int, metavar='<int>', default=11, help='integer')
parser.add_argument('-t', required=False, type=float, metavar='<float>', default=.4, help='floating point')
parser.add_argument('-s', action='store_true', help='masking')

arg = parser.parse_args()

file = arg.file
window = arg.w
threshold = arg.t

def entropy(seq, window, threshold):
	ea = 0
	et = 0
	ec = 0
	eg = 0
	for nt in seq:
		if nt == 'A': ea += 1
		elif nt == 'T': et += 1
		elif nt == 'C': ec += 1
		elif nt == 'G': eg += 1
	prob = [ea/window, et/window, ec/window, eg/window]
	h = 0
	for p in prob:
		if p == 0: continue
		h -= p*math.log2(p)
	if h < threshold: filt = True
	else: filt = False
	return filt

seqs = []
for defline, seq in mcb185.read_fasta(file):
	seq = seq.upper()
	new_seq = ''
	for i in range(0,len(seq)):
		
		if entropy(seq[i:i+window], window, threshold):
			if arg.s:
				seql = seq[i:i+window].lower()
				new_seq = new_seq[:i] + seql + new_seq[i+window:]
			else: new_seq = new_seq[:i] + 'N'*window + new_seq[i+window:]
		else: new_seq += seq[i]
	seqs.append((defline, new_seq))

for defline, seq in seqs:
	print(f'>{defline}')
	for i in range (0, len(seq),60):
		print(seq[i:i+60])

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz

python3 50dust.py -w 11 -t 1.4 -s ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz  | head
python3 50dust.py -w 11 -t 1.4 -s test.fa  | head

>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
