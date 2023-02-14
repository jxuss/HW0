# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below


import sys
import random

numb = []

for num in sys.argv[1:]:
	numb.append(int(num))

genome_size = numb[0]
read_number = numb[1]
read_length = numb[2]
# print(genome_size, read_number, read_length)
"""

genome_size = 1000
read_number = 100
read_length = 100
print(genome_size, read_number, read_length)
"""

gene = [0] * genome_size
for i in range(read_number):
	read = random.randint(1, genome_size - read_length)
	for j in range(read_length):
		gene[read+j] +=1
	
geneseq = gene[read_length:genome_size-read_length]
		# = gene[read_length : -read_length]

avg = sum(geneseq)/len(geneseq)
print(min(geneseq), max(geneseq), f'{avg:.5f}')



"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375


"""
