# Type casting is a way to convert a variable from one data type to another data type.
# In Python, we can use the following functions to convert a variable from one data type to another:
# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
data = "10"
print(type(data))

data = int(data)
print(type(data))