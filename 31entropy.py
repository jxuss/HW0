# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

numb = []
for num in sys.argv[1:]:
	numb.append(float(num))
assert (math.isclose(sum(numb),1.0))

H = 0
# print(numb)
for x in numb : 
	H += - x * math.log2(x)

print (f'{H:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
