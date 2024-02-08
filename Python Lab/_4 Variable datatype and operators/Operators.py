"""
Operators are a kind of entity that operators one or more than one operand and produces a complete different or
may be same answers

We have several kinds of operators like,
"""
# Arithmetic Operators:

# Used for basic mathematical operations.
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus (Give only reminder)
print(a ** b)  # Exponentiation (a^b)
print(a // b)  # Floor division (Division where reminder is ignored only quotient is printed)

# One extra data we can also use '+' as concatenate operator
print("I" + "am" + "boy")  # It will concatenate all the strings

# Comparison Operators:  (Used to compare between more than one values)
a = 10
b = 5
print(a == b)  # a Equal to b
print(a != b)  # a Not equal to b
print(a > b)  # a Greater than b
print(a < b)  # a Less than b
print(a >= b)  # a Greater than or equal to b
print(a <= b)  # a Less than or equal to b

# Bitwise Operators: Used to perform bitwise operations on integers

a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary
print(a & b)  # Bitwise AND (Return true if and only if both are true)
print(a | b)  # Bitwise OR (Return true if One of the value is true)
print(a ^ b)  # Bitwise XOR
print(~a)  # Bitwise NOT (Return the compliment)
print(a << 2)  # Bitwise left shift (Shifted the bits to the left by 2) It's equivalent to x * (2 ** n). [n == 2]
print(a >> 2)  # Bitwise right shift (Shifted the bits to the right by 2) It's equivalent to x // (2 ** n). [n == 2]

# Assignment Operators: Used to assign values to variables
a = 10
b = 5
a += b  # Equivalent to: a = a + b
print(a)
a -= b  # a = a-b
print(a)
a *= b  # a=a*b
print(a)
a **= b  # a=a**b (a=a^b)
print(a)
a /= b  # a=a/b
print(a)
a //= b  # a=a//b
print(a)
a %= b  # a=a%b
print(a)

# Here it will give an error, but it is part if assignment operator
# a &= b  # a=a&b
# print(a)
# a |= b  # a=a|b
# print(a)
# a ^= b  # a=a^b
# print(a)
# a >>= b  # a=a>>b
# print(a)
# a <<= b  # a=a<<b
# print(a)

# Logical Operators: Used to combine conditional statements

x = True
y = False
print(x and y)  # Logical AND
print(x or y)  # Logical OR
print(not x)  # Logical NOT

# Membership Operators:  Used to test if a sequence is presented in an object
x = [1, 2, 3, 4, 5]  # We will learn about this datatype later
print(3 in x)  # True As 3 is present in the list
print(6 not in x)  # True As 6 is not present in the list

# Identity Operators: Used to compare the memory locations of two objects
# We don't need to worry we will learn about this later
a = [1, 2, 3]
b = a
print(a is b)  # True As both now act as a same datatype
print(a is not b)  # False
