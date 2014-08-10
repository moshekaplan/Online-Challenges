"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time

def get_divisors(number):
  divisors = []
  # Should really make this sqrt, oh well
  for i in xrange(1,number):
    if number % i == 0:
      divisors.append(i)
  return divisors

def get_property(number):
  divisor_sum = sum(get_divisors(number))
  if divisor_sum == number:
    return "perfect"
  elif divisor_sum > number:
    return "abundant"
  else:
    return "deficient"

# If performance is important, limit this to non-prime numbers.
# Then, possibly use memoization to speed this up some more?
def get_abundant_numbers():
  abundant_numbers = [] 
  for number in xrange(1,28124):
    if get_property(number) == "abundant":
      abundant_numbers.append(number)
  return abundant_numbers

def sum_of_two_exists(goal, numbers):
  for i in xrange(len(numbers)):
    # Once our number is larger than the sum, there's no point in continuing
    if numbers[i] > goal:
        break
    
    for j in xrange(i, len(numbers)):
      # If this number is larger than the sum, there's no point in continuing
      if numbers[j] > goal:
        break

      # If the two numbers are equal, we found a sum for `number`
      # Then, we should break out of both loops
      if numbers[i] + numbers[j] == goal:
        return True
  return False
  
start = time.time()
abundant_numbers = get_abundant_numbers()
print len(abundant_numbers)

could_not_be_made_from_sum = []
sums = set()
for i in abundant_numbers:
  for j in abundant_numbers:
    sums.add(i+j)
    
for number in xrange(28124):
  if number % 100 == 0:
    print number
    
  # If we couldn't find the number, we should add it to the list
  if not sum_of_two_exists(number,abundant_numbers) :
    could_not_be_made_from_sum.append(number)

end = time.time()
    
print len(could_not_be_made_from_sum)
print sum(could_not_be_made_from_sum)
print "Took " + str(end-start)

