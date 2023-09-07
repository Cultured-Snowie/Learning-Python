# We can find the length of a string using len() function.
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# A string is essentially a sequence of characters also called an array. 
# Thus we can access the elements of this array
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

# Note: This method of specifying the start and end index to specify a part of a string is called slicing.
# If you are going though sentences , it counts space too. (for string slicing)

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

# Strings are arrays and arrays are iterable. Thus we can loop through strings.
alphabets = "ABCDE"
for i in alphabets:
    print(i)