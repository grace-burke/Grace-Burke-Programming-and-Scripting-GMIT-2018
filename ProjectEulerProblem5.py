# Grace Burke, 01/03/2018
# Project Euler, Problem 5
# https://projecteuler.net/problem=5

i = 2520

while ((i % 11) + (i % 12) + (i % 13) + (i % 14)\
         + (i % 15) + (i % 16) + (i % 17) + \
         (i % 18) + (i % 19) + (i % 20) != 0):
    i = i + 2520

print(i)