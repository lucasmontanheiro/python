# 01 Basic 06 Loops & Iterables


# Basic Loops

# Loop without an index
a = [1, 2, 3]
for x in a:
  print(x)

# Loop using the index
a = [1, 2, 3]
for i in range(len(a)):
  print(a[i])

# Loop through values and indices at the same time
a = [1, 2, 3]
for i, val in enumerate(a):
  print(i, val)

# Loop through pairs of elements in a and b
a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):
  print(x, y)

# Nested loop 
# (every possible combination of elements from a and b)
a = [1, 2, 3]
b = [4, 5, 6]
for x in a:
  for y in b:
    print(x, y)

# for loops with break and continue
nums = [1,2,3,4,5]
for num in nums:
  if num ==3:
    print("Found!")
    #break # It stops the loop
    continue # It doesn't print number 3
  print(num)

# Using range function
for i in range(5):
  print(i)

# Using while loop
x = 0

while x < 5:
  print(x)
  x += 1



# Intermediate Loops

# zip() coordinates multiple lists with the same lenght
import itertools
li_1 = ['a', 'b', 'c']
li_2 = [1,2]

for f,o in zip(li_1, li_2):
  print(f,o)

for f,o in itertools.zip_longest(li_1, li_2):
  print(f,o)


# enumerate() to avoid counters
for index, value in enumerate(li_1):
  print(index, value)


# Advanced Loops

# List Comprehensions
# The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code.
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. List comprehensions are not always presented to beginners, but I have included them here because you’ll most likely see them as soon as you start looking at other people’s code. The following example builds the same list of square numbers you saw earlier but uses a list comprehension:

squares = [value**2 for value in range(1, 11)] 
print(squares)