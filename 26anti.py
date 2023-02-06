# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""

print('python3 26anti.py')

anti = ''

for nt in dna:
	if   nt  == 'A': anti = 'T' + anti 
	elif nt  == 'T': anti = 'A' + anti 
	elif nt  == 'C': anti = 'G' + anti 
	else           : anti = 'C' + anti 

# print(dna)
print(anti)

