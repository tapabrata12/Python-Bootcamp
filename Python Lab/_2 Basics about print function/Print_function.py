"""
In Python or any kind of programming languages, we use functions [Which does some work for us is called function]
to do our required work.

To write or declare a function we write,

      Function_Name(Arguments)

In this case to print anything we use print()

As we all know we so many things to print like text,number [integer,decimal etc.], single character, etc.
and method of printing all of these stuffs are little different.
"""

# Text/String: You can print strings (text) directly by passing them as arguments to the print() function


print("Hello, World!")  # We use double courts "" in the first bracket

# Variables: You can print the values stored in variables {Which stores some value}
x = 10
print(x)

# We can also perform some arithmatic operation directly in the print function [like +,-,*,/,etc]

y = 20
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Multiple Arguments: We can print multiple items by separating them with commas

name = "John"
age = 30
print("Name:", name, "Age:", age)

# Formatted Output: You can use string formatting to customize the output about

"""
String formatting in Python allows you to create dynamic strings by inserting variables or expressions into 
predefined templates. This helps in customizing output messages, creating user-friendly displays, and generating 
formatted data representations. There are several ways to perform string formatting in Python, including the older 
.format() method and the newer f-strings.

Or in simple language we want to put a value of a variable without ending the string then we have two options one is 
format() function and other is f-string. Let's jum to the code. 
"""

"""
Using the .format() Method: The .format() method allows you to insert variables or values into a string template 
by specifying placeholders {} which are replaced by the arguments provided to the format() method.
"""
name = "Alice"
age = 30

# Here In this example specific {} are replaced by order of the variable given in the format function

print("Name: {}, Age: {}".format(name, age))

"""
Using f-strings (Formatted String Literals): Introduced in Python 3.6, f-strings provide a more concise and 
readable way to perform string interpolation. They allow you to embed expressions directly inside string literals by 
prefixing the string with f or F and enclosing the expressions within curly braces {}.
"""
name = "Bob"
age = 25

print(f"Name: {name}, Age: {age}")  # Here before double courts we have to give a small f

"""

Key Differences:
Readability: f-strings offer more concise and readable syntax compared to the .format() method.
Expression Evaluation: f-strings allow expressions to be directly embedded, making complex string formatting more 
straightforward.
Performance: f-strings are generally faster than the .format() method.
Compatibility: f-strings are available in Python 3.6 and later versions. If you need compatibility with older versions, 
you may need to use the .format() method.

Benefits of String Formatting:
Dynamic Output: String formatting allows you to create dynamic output messages tailored to specific data.
Readable Code: Properly formatted strings enhance code readability and maintainability.
Interpolation: It enables you to insert variables and expressions into string templates, making the output more 
informative and context-aware.
In summary, string formatting in Python is a powerful feature that helps in creating well-structured and informative 
output messages, and f-strings offer a modern and efficient way to achieve this.

"""

# And the last thing in print function is parameters

"""
In Python, the print() function accepts several parameters that allow you to customize its behavior and the output 
it produces. These parameters provide flexibility in formatting and directing the printed output. Here are some 
common parameters used with the print() function
"""

"""Objects: As we all know The primary purpose of the print() function is to display objects or values. You can pass 
one or more objects separated by commas, and print() will display them in sequence."""

print("Hello", "world", 2024)

"""sep: This parameter defines the separator between the objects being printed. By default, it is a single space ' ', 
but you can customize it to any string."""

print("apple", "banana", "cherry", sep=", ")
# This line means after ending of string we will give a comma and space and star another string
print("apple", "banana", "cherry", sep="@ %")
# This line means after ending of string we will give a @ and % and star another string

"""
end: This parameter defines the string that will be printed at the end of the print() function. By default, 
it is a newline '\n', but you can change it to any string.
"""
print("Hello", end=" ")  # means a space will print after that string
print("world")

print("Hello", end="5")  # means a space will print after that string
print("world")

print("Hello", end="&^&$%&^")  # means a &^&$%&^ will print after that string
print("world")
