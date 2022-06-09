#If/Else conditions and Comparison operators
x=10
y=15

if x>y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#elif
if x>y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#Nested if
if x > 2:
    if x <=10:
        print(f'{x} is greater than two and less than or equal to 10')


#Logical operators (and, or, not)
if y>1 or y<=20:
    print(f'{y} is greater than one or less than or equal to 20')

#Membership operators(in, not in)
numbers=[1, 5, 10, 20]
if x in numbers:
    print(x in numbers)

if y not in numbers:
    print(y not in numbers)

#Identity operators(is, is not)
if x is y:
    print(x is y)

if x is not y:
    print(x is not y)