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
  