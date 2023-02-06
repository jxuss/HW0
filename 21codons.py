# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'


"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
import math

print('python3 21codons.py')
for i in range(len(dna)):
    if i % 3 == 0:
        print(dna[i:i+3])

    
    

