#Create a class
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    #Methods
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age +=1

#Extend class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 50
        self.spend = 0
        

    #Methods
    def set_balance(self, balance):
        self.balance=balance
    
    def set_spend(self, spend):
        self.spend=spend
      

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance} and I spent {self.spend}'

#Initialize user object
owen = User('Owen Mogaka', 'owenmogaka@gmail.com', 22)
#Initialize customer object
sasha = Customer('Sasha Johnson', 'sasha34@gmail.com', 25)

sasha.set_balance(500)
sasha.set_spend(300)
print(sasha.greeting())

owen.has_birthday()
print(owen.greeting())
