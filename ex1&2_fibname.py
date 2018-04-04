# Grace Burke

# A program that displays Fibonacci numbers using people's names.
# https://en.wikipedia.org/wiki/Fibonacci_number

# Code provided by Ian McLoughlin

# Exercise 1:
# In the video lectures this week we ran an example program that calculated the 30th Fibonacci number. 
# Change the program to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. 
# Take A as the number 1, B as 2, C as 3, and so on.

# Exercise 2:
# Above is a link to a program I wrote that works similarly to last week's exercise. Copy and run the program yourself. 
# Change the string variable to contain your own surname, and rerun it. 
# Can you figure out what ord() does? Try to Google it to find out. 


def fib(n):
# This function returns the nth Fibonacci number.
  i = 0
  j = 1
  n = n - 1
  # Initial values are set for variables to be used in function. These will be ammended within the function to produce the returned value.

  while n >= 0:
    i, j = j, i + j
    n = n - 1
    # The value of the input value n is decremented by 1 in each cycle of the while loop until it reaches zero, so the operations are run n times.
    # In each cycle of the while loop, the value of i is set to the previous value of j, and the value of j is set to the sum of i and j.

  return i

name = "Burke"
first = name[0]
last = name[-1]
# These lines isolate the first and last letters from the string.

firstno = ord(first)
lastno = ord(last)
# These lines provide the unicode value for the characters identified as first and last.

x = firstno + lastno

ans = fib(x)

print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


# Week 1 Discussion Post:
# My name is Grace, so the first and last letter of my name (G + E = 7 + 5) give the number  12. The 12th Fibonacci number is 144. 

# Week 2 Discussion Post:
# My surname is Burke
# The first letter B is number 66
# The last letter e is number 101
# Fibonacci number 167 is 35600075545958458963222876581316753
# Ord is a built-in Python function which returns the Unicode code point of a string. In this example ord converts the 
# first and last letters of the surname into their Unicode integer equivalents so that the relevant Fibonacci number can be calculated.
