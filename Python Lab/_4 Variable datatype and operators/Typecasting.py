"""
In Python, typecasting refers to converting a value from one data type to another. Python provides several
built-in functions for typecasting, such as int(), float(), str(), bool(), etc. Here's how you can perform
typecasting for various data types in Python:

"""
# Integer (int) conversion (Float to Integer) and (String to Integer)

float_num = 3.14
print(float_num)
print(type(float_num))  # Output: <class 'float'>
int_num = int(float_num)
print(int_num)  # Output: 3
print(type(int_num))  # Output: <class 'int'>

# String to Integer (One thing to be note is that words like a , b,c,d ,boy.cat.etc can't be converted to int )
str_num = "123"
print(str_num)
print(type(str_num))  # Output: <class 'str'>
int_num = int(str_num)
print(int_num)  # Output: 123
print(type(int_num), end="\n\n\n\n")  # Output: <class 'int'>

# Boolean Conversion

# Decimal value (float) conversion (int to float) and (String to float)

# Integer to Float
int_num = 5
print(int_num)
print(type(int_num))  # Output: <class 'int'>
float_num = float(int_num)
print(float_num)  # Output: 5.0
print(type(float_num))  # Output: <class 'float'>

# String to Float
str_num = "3.14"
print(str_num)
print(type(str_num))  # Output: <class 'str'>
float_num = float(str_num)
print(float_num)  # Output: 3.14
print(type(float_num), end="\n\n\n\n")  # Output: <class 'float'>

# String conversion (int to string) and (float to string)

# Integer to String
int_num = 123
print(int_num)
print(type(int_num))  # Output: <class 'int'>
str_num = str(int_num)
print(str_num)  # Output: '123'
print(type(str_num))  # Output: <class 'str'>

# Float to String
float_num = 3.14
print(float_num)
print(type(float_num))  # Output: <class 'float'>
str_num = str(float_num)
print(str_num)  # Output: '3.14'
print(type(str_num), end="\n\n\n\n")  # Output: <class 'str'>

# Bool conversion

# Integer to Boolean
int_num = 1
print(int_num)
print(type(int_num))
bool_val = bool(int_num)
print(bool_val)  # Output: True
print(type(bool_val))

# Float to Boolean
float_num = 0.0
print(float_num)
print(type(float_num))
bool_val = bool(float_num)
print(bool_val)  # Output: False
print(type(bool_val))

# String to Boolean
str_val = "True"
bool_val = bool(str_val)
print(bool_val)  # Output: True
print(type(bool_val), end="\n\n\n\n")

"""
We have more datastructures like set , list and tuple which also supports  the above operations but they are not covered 
in this example because it will cover when that has been taught.
"""
