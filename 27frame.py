# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'


"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""

print('python3 27frame.py')

# single loop
frame = 0
for i in range(0,len(dna),1):
	if   i % 3 == 0: frame = 0
	elif i % 3 == 1: frame = 1
	else           : frame = 2
	print (i, frame, dna[i])


# nested loops
for i in range(0,len(dna),3):
	for j in range(3):
		print(i+j,j,dna[i+j])

