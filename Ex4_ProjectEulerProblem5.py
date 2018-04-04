# Grace Burke 
# 01/03/2018

# Exercise 4
# 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. 

# Project Euler, Problem 5
# https://projecteuler.net/problem=5

i = 2520
# The initial guess value is set at 2520 as the least common multiple of 1 to 20 must also be divisible by 1 to 10, cannot be smaller tham the least common multiple of 1 to 10.

while ((i % 11) + (i % 12) + (i % 13) + (i % 14)\
         + (i % 15) + (i % 16) + (i % 17) + \
         (i % 18) + (i % 19) + (i % 20) != 0):
    i = i + 2520
    # This while loop cycles until the sum of the remainders of each number from 11 to 20 is equal to zero, which implies we have found the least common multiple.
    # Increments are made in jumps of 2520 as this is the least common multiple of 1 to 10.
    
print(i)