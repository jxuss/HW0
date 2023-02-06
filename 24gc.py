# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'


"""
python3 24gc.py
0.42
"""

import math
print('python3 24gc.py')

n = 0

for i in range(len(dna)):
    gc = dna[i]
    if gc == 'C' or gc == 'G':
        n = n+1
    # print(gc,n)
gc_precent = n / len(dna)
# print(gc_precent)

print(f'{gc_precent:.2f}')
