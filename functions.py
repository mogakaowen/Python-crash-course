#Create a function
def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

#Return values
def getSum(num1, num2):
    total=num1+num2
    return total
num=getSum(3, 4)
print(num)

#Lambda function
getSum= lambda num1, num2: num1 + num2

print(getSum(10, 3))


y=9//2
print(y)
