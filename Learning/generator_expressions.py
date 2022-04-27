# HOW AND WHERE TO USE GENERATORS

# Generators can be used in similar situations as lists, but generate items one at a time.
# This means generators don't use up memory by storing data. They create one item at a time, but don't store the values

my_list = [x for x in range(0,10)]
my_generator = (x for x in range(0, 10))

# See output for difference

print(my_list)

# For the generator it didn't actually create the value, but some generator object. 
print(my_generator)

# If we want to get values from this genexpress, we can use next()
# This is called lazy evaluation: a generator only gets the next item when asked for it
print(next(my_generator))
print(next(my_generator))

# The take the values used by next() into account. This for loop will start at 2  
for item_left in my_generator:
  print(item_left)

# This tries toe access a list item which has already given out. gives back an error. to loop again trough generator expression you need to create a new one like above
# print(next(my_generator))

# REASONS TO USE GENERATORS

# Use generators when you don't know how many results you need or don't want to store all results in memory.

# You can also Yield in functions to them into generators by using the Yield keyword. See other tutorial.