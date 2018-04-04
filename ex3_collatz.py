# Grace Burke 
# 08/02/2018

# Exercise 3:
# Complete the exercise discussed in the Collatz conjecture video by writing a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. 
# At each iteration, the current value of the integer should be printed to the screen. 
# You can specify in your code the starting value of 17. 
# If you wish to enhance your program, have the program ask the user for the integer instead of specifying a value at the start of your code.

# https://en.wikipedia.org/wiki/Collatz_conjecture

x = int(input("Please enter an integer: "))
# This line requests an input value from the user.

while x > 1:
    # This while loop ensures that the operations below are carried out until the input value reaches 1, as specified.
    if x % 2 == 0:
        # This if statement checks if the value is even, if so it carries out the operation for even values.
        x = x//2
    else:
        # If value is not even, if statement carries out operation for odd values. 
        x = 3*x + 1
    print (x)
    # This line prints the value at each cycle of the while loop.
