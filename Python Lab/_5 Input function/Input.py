"""
Basic Usage:
The input() function in Python is used to accept user input from the keyboard during program execution. It allows
a program to pause and wait for the user to enter some data, which can then be processed or used in various ways
within the program. Here's an in-depth explanation along with consecutive examples
"""
# Example 1: Basic usage of input() function
name = input("Enter your name: ")
print("Hello,", name)

'''
Explanation:

The input() function takes a single argument, which is the prompt displayed to the user.
In this example, the prompt is "Enter your name: ".
Whatever the user types in response to the prompt is stored in the variable name.
The program then prints a greeting message using the entered name.

Also one thing is to be discussed that if this name variable not be given then that input function stores that input in 
somewhere in memory location 
'''
# Type Conversion:
# Example 2: Type conversion using input() function
age = input("Enter your age: ")
age = int(age)
print("You will be", age + 1, "years old next year.")

'''
Explanation:

By default, the input() function returns user input as a string.
In this example, we accept the user's age as input.
Since we want to perform arithmetic operations on the age (add 1), we convert the input to an integer using int().
Then we use the value in arithmetic operations.
'''
# Handling Different Data Types:
# Example 3: Handling different data types using input() function
num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print("The sum is:", result)

'''
Explanation:

We can directly convert the user input to the desired data type within the input() function.
In this example, the first input is converted to an integer using int(), and the second input is converted to a float 
using float().
The program then performs addition on the numbers and prints the result.
'''

# !!! WE WILL LEARN IT ABOUT LATER CODE SNIPPETS FOR NOW WE CAN IGNORE IT !!!

# Input Validation:
# Example 4: Input validation using input() function
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Please enter a valid age.")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid integer for age.")

print("Your age is:", age)

'''
Explanation:

Input validation ensures that the user enters appropriate data.
In this example, we use a while loop to repeatedly prompt the user until a valid age is entered.
We use a try-except block to handle non-integer inputs gracefully.
If the input is not an integer or if it's negative, appropriate error messages are displayed, and the loop continues.
If the input is valid, the loop breaks, and the program proceeds.
'''

"""
These examples illustrate different aspects of using the input() function in Python along with various techniques for 
processing and validating user input.
"""