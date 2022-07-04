#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc. If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

#Example 1
a = ("John", "Charles", "Mike", "Ross")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(list(x))

#Example 2
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]
result = zip(languages, versions)
print(list(result))

#Example 3
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()
print(list(result))

# Two iterables are passed
result = zip(number_list, str_list)
print(set(result))

#Example 4: Unzipping the Value Using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('coordinate =', c)
print('value =', v)