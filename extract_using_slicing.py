#Program to extract specific words from a string by slicing
line = "I love Python Programming Language"
start = line.index('Programming')
length = len('Programming')
print(start)
print(length)
print(line[start:start+length])
