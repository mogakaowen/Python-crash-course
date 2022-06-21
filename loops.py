#For loop-used for iterations
people=['John', 'Owen', 'Carol', 'Susan']

for person in people:
    print(f'Current person:{person}')

#Break(Stops before the stated person)
for person in people:
    if person=='Carol':
        break
    print(f'Current person:{person}')

#Continue(jumps the stated person)
for person in people:
    if person=='Carol':
        continue
    print(f'Current person:{person}')

#Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

#While loops
count=0
while count <= 10:
    print(f'Count: {count}')
    count +=1
  
#More on loops
tab = [i for i in range(0,8)]
def tabx():
    x=1
    for i in tab:
        boundary = ' \ '
        if x%2==0:
            boundary=' | '
        x+=1    
        print(boundary)
tabx()