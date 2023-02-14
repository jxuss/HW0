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
"""
numb = []
for num in sys.argv[1:]:
    numb.append(float(num))
print(numb)
"""


# print(day)

total = 0
for t in range(0,100000):
    day = [0] * 365
    # print(day)
    bday = 0
    for i in (1,23):
        d = random.randint(0,364)
        # print(d)
        day[d] += 1
        if day[d] > 1:
            bday = 1
    total += bday

prob = total/100000
print(f'{prob:.3f}')





    

"""
python3 33birthday.py 365 23
0.571
"""

