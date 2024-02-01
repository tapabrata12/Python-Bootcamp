r"""
Escape sequences in Python are special sequences of characters used to represent certain non-printable characters or to
add special formatting to strings.
They are preceded by a backslash (\) character.
Here are some common escape sequences used in Python
"""

r"""
\n: Represents a newline character. It is used to move the cursor to the next line.
\t: Represents a tab character. It is used to insert horizontal tab spaces.
\r: Represents a carriage return character. It moves the cursor to the beginning of the line without advancing to the 
next line.
\: Represents a single backslash character.
\b: Represents a backspace character. It moves the cursor one character back.
**': Represents a single quote character (').
": Represents a double quote character (").
\xhh: Represents a character with hexadecimal value hh.
\ooo: Represents a character with octal value ooo.
\uchar: Represents a Unicode character with hexadecimal value hhhh.
\Uhhhhhhhh: Represents a Unicode character with hexadecimal value hhhhhhhh.
"""
# Basically, we mostly used top two or three

print("Hello\nWorld")  # Output: Hello
#         World

print("Hello\tWorld")  # Output: Hello    World

print("Hello\rWorld")  # Output: World

print("This is a single backslash: \\")  # Output: This is a single backslash: \

print("This is a backspace\b")  # Output: This is a backspac

print('This is a single quote: \'')  # Output: This is a single quote: '

print("This is a double quote: \"")  # Output: This is a double quote: "

print("\x48\x65\x6c\x6c\x6f")  # Output: Hello

print("\110\145\154\154\157")  # Output: Hello

print("\u0048\u0065\u006c\u006c\u006f")  # Output: Hello

print("\U00000048\U00000065\U0000006c\U0000006c\U0000006f")  # Output: Hello

# Sometimes we want to print the backslash character as it is, we will do this via raw string

r"""
Raw string starts with [ r"Your content" ] A raw string in programming refers to a string literal that is prefixed with 
an 'r' (or 'R' in some languages), which tells the interpreter or compiler to interpret the string contents literally, 
without treating backslashes ('') as escape characters. Raw strings are particularly useful when dealing with regular 
expressions, file paths, and any other string where backslashes are common and need to be interpreted as literal 
characters rather than escape characters.
"""

print(r"Hello\nWorld")

print(r"Hello\tWorld")

print(r"Hello\rWorld")

print(r"This is a single backslash: \\")

print(r"This is a backspace\b")

print(r'This is a single quote: \'')

print(r"This is a double quote: \"")

print(r"\x48\x65\x6c\x6c\x6f")

print(r"\110\145\154\154\157")

print(r"\u0048\u0065\u006c\u006c\u006f")

print(r"\U00000048\U00000065\U0000006c\U0000006c\U0000006f")