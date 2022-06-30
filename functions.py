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

#lambda arguments: expression
# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

#The filter() function in Python takes in a function and a list as arguments. The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
# Program to filter out only the even items from a list.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

#The map() function in Python takes in a function and a list.The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)