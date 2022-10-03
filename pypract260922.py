def name(firstName, age):
    print("Your name is " + firstName + " you are " + str(age) + " years old")

name("Ayomide", 17)

def add(par1,par2):
    print(int(par1) + int(par2))
    
def subtract(par1,par2):
    print(int(par1) - int(par2))

def multiply(par1,par2):
    print(int(par1) * int(par2))

def divide(par1,par2):
    if(par1 == 0 or par2 == 0):
        print("Sorry you can not carry out this maths operation")
    else:
        print(int(par1) / int(par2))
n = 0 
while n < 5:
    print(n)
    n = n + 1

def test():
    x = int(input("Enter a number"))
    while x != 0:
        if x == 0:
            break
        else:
             print (x)
             x = int(input("Enter a number"))
num = 10
while num !=0:
    if num % 2 == 0:
        print("the number is even")
        num = num - 1 
    elif (num % 2 != 0):
        print("the number is odd")
        num = num - 1 
 
list = ["japan", "italy","spain"]
def print_countries(theList):
    for i in theList:
        print(i)
def print_range(theRange):
    x = range(theRange)
    for i in x:
        print(i)

def infi():
    if 1 == 1:
        print("Error")
add(12,2)
subtract(10,5)
multiply(3,10)
divide(10,3)
print_countries(list)
print_range(10)
test()
