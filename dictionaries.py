#Create dict
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30

}

#Use a constructor
#person2=dict(first_name='Jane', last_name='Doe')

#Get a value
print(person['first_name'])
print(person.get('last_name'))

#Add value
person['phone']='0700000000'

print(person)

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

#Copy dict
person2=person.copy()
person2['city']='Boston'

print (person2)

#Remove an item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get length
print(len(person2))
print (person)

#List of dictionaries
people=[
    {'name':'Mary', 'age' :30},
    {'name':'Faith', 'age' :24},
    {'name':'Sam', 'age' :20}
]

print(people)
print(people[1] ['name'])