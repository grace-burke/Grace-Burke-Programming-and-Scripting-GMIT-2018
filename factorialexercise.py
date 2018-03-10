# Grace Burke, 10/03/2018
# Exercise 6

# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial.
# You should, in your script, test the function by calling it with the values 5, 7, and 10.

def factorialfunction(x):
    result = 1
    for i in range(1, (x+1)):
        result = result * i
    return result

print ("The factorial of 5 is", factorialfunction(5))
print ("The factorial of 7 is", factorialfunction(7))
print ("The factorial of 10 is", factorialfunction(10))