def binary_search_recursive(a_list, first, last, item):

    if last>=first:
        i = (first + last) // 2

        if a_list[i] == item:
            return 'The number {item} was found at position {i}'.format(item=item, i=i)

        elif a_list[i] > item:
            last=i-1
            return binary_search_recursive(a_list, first, last, item)

        else:
            first=i+1
            return binary_search_recursive(a_list, first, last, item)

    else:
        return 'The number {item} was not found in the list'.format(item=item)

a_list=[1,2,3,4,5,6,7,8]
item=input('Enter element to be found: ')
item=int(item)
first = 0
last = len(a_list) - 1

result=binary_search_recursive(a_list, first, last, item)
print(result)

def binary_search(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    
   
    while first <= last:
        i = (first + last) / 2
        i=int(i)
        if a_list[i] == item:
            return 'The number {item} was found at position {i}'.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
    return 'The number {item} was not found in the list'.format(item=item)

a_list=[1,2,3,4,5,6,7,8]
item=input('Enter element to be found: ')
item=int(item)


result=binary_search(a_list, item)

print(result)