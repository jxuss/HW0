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
# python3 50dust.py -w 11 -t 1.4 -s testfile.fa  | head
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='Calculate sequence entropy and mask in lowercase.')
parser.add_argument('-w', metavar='window_size', type=int, default=11,
					help='Size of window used to calculate entropy. Default is 11.')
parser.add_argument('-t', metavar='threshold', type=float, default=1.4,
					help='Masking threshold for entropy. Default is 1.4.')
parser.add_argument('-s', '--lowercase-masking', action='store_true',
					help='Use lowercase masking for nucleotides below the entropy threshold.')
parser.add_argument('file', metavar='path_to_file',
					help='Path to input FASTA file.')
args = parser.parse_args()

def convert(nucleotide):
	if args.lowercase_masking:
		return nucleotide.lower()
	else:
		return nucleotide.upper()

alphabet = 'ACGT'
mask_value = args.w // 2

for name, seq in mcb185.read_fasta(args.file):
	seq_list = list(seq.upper())  
	window = seq[:args.w]  

	for i in range(len(seq) - args.w):
		H = [0] * len(alphabet)  
		count = [0] * len(alphabet)  
		p = [0] * len(alphabet)  #
		for j in range(args.w):
			count[alphabet.find(window[j])] += 1
		for j in range(len(alphabet)):
			p[j] = count[j] / args.w
			if p[j] != 0:
				H[j] -= p[j] * math.log2(p[j])
		if sum(H) < args.t:
			seq_list[i + mask_value] = convert(seq_list[i + mask_value])

		count[alphabet.find(window[0])] -= 1
		window = window[1:] + seq[i + args.w]
		count[alphabet.find(window[-1])] += 1

		if (i + 1) % 60 == 0:
			seq_out = ''.join(seq_list[i + 1 - 60:i + 1]) + '\n'
			print(seq_out, end='')
	seq_out = ''.join(seq_list[(len(seq)//60)*60:])
	if len(seq_out) > 0:
		print(seq_out)






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
