#!/usr/bin/env python
#Encoding: UTF-8

# Written for Python 2.7

"""\
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from string import lowercase

values = {}
for val, char in enumerate(lowercase):
    values[char] = val+1

names = sorted(open('names.txt').read().split(','))

def value(word):
    sum = 0
    for char in word.lower():
        if char in values:    
            sum += values[char]
    return sum

sum = 0
for i, name in enumerate(names):
    sum += (i+1)*value(name)
print sum
