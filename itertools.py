#Infinite Iterators 
from itertools import count

def counting(start, step):
    counter = count(start, step)
    for i in counter:
        print(i, end=" ")  #Counts in the steps of 5
        if i == 20:
            break

counting(0, 5)

from itertools import repeat
def repeating(element, max_repeats):
    repeater = repeat(element, max_repeats)
    for i in repeater:
        print(i, end=" ") #Repeats the output max_repeats times

repeating("You", 4)

from itertools import cycle
def cycling(elements):
    cycler = cycle(elements)
    i=0
    while i < 10:
        print(next(cycler), end=" ") #Cycles the elements in a loop the desired number of times
        i += 1

cycling("ABCDEFG")

#Terminating iterators
from itertools import accumulate
def accumulating(elements):
    accumulator = accumulate(elements)
    print(list(accumulator)) #Prints the sum of elements at that index and below 

accumulating([1,2,3,4,5])

from itertools import chain
def chaining(elements1, elements2):
    chained = chain(elements1, elements2)
    print(list(chained))     #Combines the given elements like a chain in one list 

chaining("ABC", "GEF")

def chain_from_iterable_example(iterable):
    chained = chain.from_iterable(iterable)
    print(list(chained))

chain_from_iterable_example([[1,2,3], [4,5,6], [7,8,9]])

from itertools import compress
def compressor(data, selectors):
    compressed = compress(data, selectors)
    print(list(compressed))  #Prints only the True elements

compressor([['A', 'B','C'], [1, 2, 3]],[True,True])

from itertools import pairwise
def pairwise_example(iterable):
    paired = pairwise(iterable)
    print(list(paired))       #Prints pairs

pairwise_example([1, 2, 3, 4, 5])

#Combinatoric iterators
from itertools import product
def product_example(elements1, elements2):
    result = product(elements1, elements2)
    print(list(result))       #Prints cartesian product

product_example([1, 2, 3], ['a', 'b', 'c'])

from itertools import permutations
def permutation(elements, size):
    result = permutations(elements, size)
    print(list(result))

permutation("ABCD",2)

from itertools import combinations
def combination(elements, size):
    result = combinations(elements, size)
    print(list(result))

combination("ABCD",3)