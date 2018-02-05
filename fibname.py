# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Burke"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
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
