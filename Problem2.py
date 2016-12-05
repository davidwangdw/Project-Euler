#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import math

def F(n):
	return ((1+math.sqrt(5))**n - (1-math.sqrt(5))**n) / (2**n*math.sqrt(5))

totalSum = 0
i = 1

while (F(i) < 4000000):

	if (int(F(i))%2 == 0):
		totalSum += F(i)

	i += 1

print(totalSum)