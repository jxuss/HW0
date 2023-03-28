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

parser = argparse.ArgumentParser(description='Entropy')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('-w', required=False, type=int, metavar='<int>', default=11, help='window size')
parser.add_argument('-t', required=False, type=float, metavar='<float>', default=1.4, help='entropy threshold')
parser.add_argument('-s', action='store_true', help='on/off switch for lowercase masking')
arg = parser.parse_args()

c = 'ACGT'
m = arg.w // 2

if arg.s ==True:
	def convert(nucleotide):
		return nucleotide.lower()
else:
	def convert(nucleotide):
		return 'N'

for name, seq in mcb185.read_fasta(arg.file):
	seql = list(seq.upper())
	win = seq[:arg.w]
	H = [0] * len(c)
	p = [0] * len(c)
	count = [0] * len(c)
	seqout = ''

	for i in range(len(c)):
		count[i] = win.count(c[i])
		p[i] = count[i] / arg.w
		if p[i] != 0:
			H[i] -= p[i] * math.log2(p[i])


	for i in range(len(seq) - arg.w):
		if sum(H) < arg.t:
			seql[i + m] = convert(seql[i + m])


		ps = c.find(win[0])
		count[ps] -= 1
		p[ps] = count[ps] / arg.w
		win = win[1:] + seq[i + arg.w]
		pe = c.find(win[-1])
		count[pe] += 1
		p[pe] = count[pe] / arg.w


		for i in range(2):
			if p[ps] != 0:
				H[ps] =- p[ps] * math.log2(p[ps])
			else:
				H[ps] = 0
			ps = pe


	print('>' + name)
	print(''.join(seql))






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
