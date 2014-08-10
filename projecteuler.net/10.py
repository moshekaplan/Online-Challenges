import math
# Our constant, of sum of all prime numbers until
amt = 2000000

numbers = []
for i in range(amt):
	numbers.append(i)
numbers[1] = 0

sqrt_amt = math.sqrt(amt)
p = 2
while (p*p < amt):
	for i in range(2*p, amt, p): # start at p, going up p each time, end at amt	
		numbers[i] = 0
	if p % 10 == 0:
		print p
	p+=1

sum = 0
for i in numbers:
	sum = sum + i
print sum
