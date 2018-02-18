# Grace Burke 08/02/2018
# https://en.wikipedia.org/wiki/Collatz_conjecture

x = int(input("Please enter an integer: "))

while x > 1:
    if x % 2 == 0:
        x = x//2
    else:
        x = 3*x + 1
    print (x)
    
