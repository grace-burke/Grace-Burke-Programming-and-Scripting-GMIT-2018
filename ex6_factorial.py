# Grace Burke, 10/03/2018
# Exercise 6

# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial.
# You should, in your script, test the function by calling it with the values 5, 7, and 10.


def factorial(x):
    # This function takes input x and returns the product of every integer from 1 to input value x.

    result = 1
    # The value to be returned (result) is initially set to 1, it will be ammended in the following for statement to produce the correct result.
 
    for i in range(1, (x+1)):
    # This for statement will multiply result by each number from 1 to the input value x sequentially.
        result = result * i
    
    return result
    # Once the for statement has cycled through each value in the range, result is returned and the function ends.


print ("The factorial of 5 is", factorial(5))
print ("The factorial of 7 is", factorial(7))
print ("The factorial of 10 is", factorial(10))