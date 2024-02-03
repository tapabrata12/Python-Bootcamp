"""
In Python, a data type is a classification that specifies which type of value a variable can hold. Python is a
dynamically typed language, which means that you don't need to explicitly declare the data type of variable; the
interpreter infers it based on the value assigned to the variable. However, Python does have built-in data types,
and you can use them to specify the type of data a variable should hold.

One extra thing, type() helps to show the datatype of that specific datatype.
"""
#  int: Integer type, represents whole numbers (e.g., 5, -3, 0).

x = 5
print(x)
print(type(x))

# float: Floating-point type, represents decimal numbers (e.g., 3.14, -0.5).
y = 3.14
print(y)
print(type(y))

""" To declare string datatype, we have to give '' or "" 
str: String type, represents sequences of characters (e.g., "hello", 'Python'). """
z = "Hello, Python!"
print(z)
print(type(z))

# bool: Boolean type, represents truth values (True or False).
a = True
print(a)
print(type(a))

"""In Python, the complex data type represents complex numbers, which are numbers with both real and imaginary parts. 
Complex numbers are written with a real part and an imaginary part, expressed as a + bj, where a is the real part, 
b is the imaginary part, and j is the square root of -1 (also denoted as i in mathematics).

Here's an example of using complex numbers in Python:

"""
# Creating complex numbers
z1 = 2 + 3j  # 2 is the real part, 3 is the imaginary part
z2 = 4 - 5j  # 4 is the real part, -5 is the imaginary part

# Addition
result_add = z1 + z2
print("Addition:", result_add)  # Output: (6-2j)

# Subtraction
result_sub = z1 - z2
print("Subtraction:", result_sub)  # Output: (-2+8j)

# Multiplication
result_mul = z1 * z2
print("Multiplication:", result_mul)  # Output: (23+2j)

# Division
result_div = z1 / z2
print("Division:", result_div)  # Output: (-0.17073170731707318+0.5365853658536586j)

# Real and Imaginary Parts
print("Real part of z1:", z1.real)  # Output: 2.0
print("Imaginary part of z1:", z1.imag)  # Output: 3.0

"""
We have some more datatypes like list, set, tuple but we will discuss separately later in our upcoming videos
"""
