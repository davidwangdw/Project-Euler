# Project Euler - Problem 1

# David Wang - 12/1/2016

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# We create an array that will house all multiples of 3 or 5, then loop through the array and sum all the integers

idx = 0
count = 0
while (idx < 1000):
    if idx%3 == 0 or idx%5 == 0:
        count += idx
        
    idx += 1
    
print count
    