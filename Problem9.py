import math

a = 1
b = 1
c = 1

while a < 332:
	b = 1
	while b < 498:
		c = 1
		while c < 998:
			if a**2 + b**2 == c**2 and a + b + c == 1000:
				print(a*b*c)
				print(a)
				print(b)
				print(c)
			c += 1
		b += 1
	a += 1
