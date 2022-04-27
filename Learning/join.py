# delimiter
d = ' '

# From string to list
# data
data = 'this is data'
# returns list where each word of data is a list element
print(data.split(d))

# From list to string
data = ['this', 'is', 'data']
print(d.join(data))

# print("".join(data))
# print(" ".join(data))
# print("-".join(data))

# Convert to str before printing.
data = ['this', 'is', 'data', 5, 10]
# This is known as a generator expression. See 
print(d.join(str(i) for i in data))
