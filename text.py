'''
def calculate(num1, num2):

    result = num1 + num2
    print(result)

try:
    calculate(int(input("Enter value: ")),int(input("Enter value2: ")))
except:
    print("Something went wrong")

#This code is for file reading
just_file = open("just.txt", "a")
for files in just_file:
    print(files)
just_file.write("This is the new line")

just_file.close()
'''


#This code creates a class

#This is code is to get hinheritance from another file. I hinretite class from new.py named Persons to Cat class.
from new import Person
class Cat(Person):
    pass

p1 = Cat()
print(p1.last)
print(p1.aged)
#The code ends here


class DOG():
    def __init__(self,name,age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = int(input("Enter your age in integer: "))
p1 = DOG(name,age)
print("Hello " + p1.name + " Welcome to my site, You are ",  p1.age , "Years old" )


