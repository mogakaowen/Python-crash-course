
def sum():
    
    t=0
    ans=0
    numbers=int(input('How many numbers do you wanna add? '))
    n=float(input('Enter a number: '))
 
    while t<numbers-1:
        ans=ans+n
        t+=1
        n=float(input('Enter another number: '))
    return [ans, t+1]

list=sum()
print('Sum= ', list[0], 'Inputs=',list[1])