import json

#Sample JSON
userJSON= '{"first_name": "John" , "last_name": "Doe" ,"age": 28}'

#Parse to dict
user=json.loads(userJSON)

print(user['last_name'])
print(user)

car={'make':'Ford', 'model':'Mustang', 'year':1970}

carJSON=json.dumps(car)

print(carJSON)