# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
#cd ~/Code/HWnow 
import sys
import math

# print(sys.argv)

numb = []
for num in sys.argv[1:]:
    numb.append(float(num))
numb.sort()
print(numb)

mean = sum(numb) / len(numb)

var = 0
sd = 0
for x in numb:
    var += ((x - mean))**2 
sd = (var/len(numb))**0.5
# print(var, sd)

midpoint = len(numb)//2
if len(numb) % 2 ==1:
    median = numb[midpoint]
else:
    median = (numb[midpoint] + numb[midpoint-1])/2

# print(median)

print('Count:', f'{len(numb):.1f}','\nMinimum:', f'{min(numb):.1f}', '\nMaximum:', f'{max(numb):.1f}')
print('Mean:',f'{mean:.3f}' )
print('Std. dev:',f'{sd:.3f}')
print('Median',f'{median:.3f}')



"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000


"""

