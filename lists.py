#Create list
numbers=[1, 2, 3, 4, 5, 6]
fruits=['Apples', 'Oranges', 'Pears', 'Grapes']

#Use a constructor
#numbers2=((1, 2, 3, 4, 5))

#Get a value
print(fruits[2])

#Length
print(len(fruits))

#Append to list
fruits.append('Mangoes')

#Removes from list
fruits.remove('Pears')

#Insert into list
fruits.insert(2, 'Strawberries')

#Change value
fruits[0]='Watermelons'

#Remove with pop
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

print(fruits)
