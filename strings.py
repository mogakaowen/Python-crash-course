from __future__ import print_function


name='mogaka'
age=22

#Concatenate
print('Hello,my name is ' +name +' and I am ' + str(age))

#String formatting
#Arguments by position
print("My name is {name} and I am {age}" .format(name=name, age=age))

#F-strings
print(f'My name is {name} and I am {age}')

#String methods

s='hello world'

#Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())