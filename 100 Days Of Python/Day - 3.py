# Variable is like a container that holds data.
# Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
a = 1
b = True
c = "Hello"
d = None

# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:
a = 1
print(type(a))
b = "1"
print(type(b))

# By default, python provides the following built-in data types:

# Numeric data: int, float, complex
# Text data: str
# Boolean data: True or False

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)