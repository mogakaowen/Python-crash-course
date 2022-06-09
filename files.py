#Open a file
import os


myFile=open('myfile.txt', 'w')

#Get some info
print('Name:', myFile.name)
print('Is Closed:', myFile.closed)
print('Opening Mode:', myFile.mode)

#Write to file
myFile.write('I wanna learn python')
myFile.write(' and Javascript.')
myFile.close()

#Append to file
myFile=open('myFile.txt', 'a')
myFile.write(' Will I?')
myFile.write(' Stay tuned')
myFile.close()

#Read from file
myFile=open('myFile.txt', 'r+')
text = myFile.read()
print(text)