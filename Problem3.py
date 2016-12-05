# What is the largest prime factor of the number 600851475143 ?

import math

num = 600851475143
prime = 1
i = 1
j = 1

while i < num:
	if num%i == 0:
		while j<i:
			if i%j == 0:
				prime = i
			j += 1
	i += 1
print(prime)