"""
Variable is simply like a container that stores a value.
Variable Assignment: You can assign values to variables using the assignment operator =

Variable Naming Rules:
Variable names must start with a letter or underscore (_).
The remainder of your variable name may consist of letters, numbers, and underscores.
Variable names are case-sensitive.
"""

my_variable = 42
_a = 42

# 1a = 42 It will through an error
# $ = 42 It will through an error
# %g = 42 It will through an error

"""
In Python there is a concept of reference variable so when write _a = 42 and  my_variable = 42
so actually in memory there made a place type, that obj and reference no: are made and when we input 
same object so both are pointing to the same thing _ --> 42 <-- my_variable just reference no:
are updated 1 to 2
"""
# We can also know the memory address of the variable via id() method
print(id(_a))
print(id(my_variable))

# In this case both are pointing same object so memory address for variable are same
