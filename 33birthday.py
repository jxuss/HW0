# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import random 

numb = []

for num in sys.argv[1:]:
	numb.append(int(num))
# print(numb)
days = numb[0]
people = numb [1]

"""
days = 365
people = 23
"""

trials = 10000
total = 0


for t in range(0,trials):
	day = [0] * days
	# print(day)
	bday = False
	for i in range(people):
		d = random.randint(0,days-1)
		# print(d)
		day[d] += 1
		if day[d] == 2:
			bday = True
			break
	if bday: total +=1 

prob = total/trials
print(f'{prob:.3f}')





	

"""
python3 33birthday.py 365 23
0.571
"""

