# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library


"""
python3 22sumfac.py
5 15 120
"""

import math
print('python3 22sumfac.py')

k=5

s = 0
f = 1
for i in range(1, k+1, 1): 
	#print(i, 'indicator')
	s = s + i
	f = f * i
	#print(k, s, f)
	if i == k:
		break
		
print(k, s, f)