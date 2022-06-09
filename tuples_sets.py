#Create tuple
fruits=('Apples', 'Oranges', 'Grapes')
fruits2=('Watermelon',)

#print(fruits, fruits2, type(fruits2))

#Get value
print(fruits[2])

#fruits[0]='Pears'

#Delete tuple
del fruits2

#Get length
print(len(fruits))


#Create a set
fruits_set={'Apples', 'Oranges', 'Mangoes'}

#Check if in set
print('Pears' in fruits_set)

#Add to set
fruits_set.add('Pears')

#Remove from set
fruits_set.remove('Pears')

#Clear set
fruits_set.clear()


#Delete set
del fruits_set

print(fruits_set)