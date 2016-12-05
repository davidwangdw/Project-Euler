# Problem 6 - Project Euler

import math

sum1 = 0
sum2 = 0
idx = 0

while idx < 101:
	sum1 += idx**2
	sum2 += idx
	idx += 1

print(sum2**2 - sum1)