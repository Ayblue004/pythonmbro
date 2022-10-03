"""
data = "Hello, I am going into a new file"
data2 = "I am a new line of words that mean nothing"

def write():
    with open('data.txt', 'w') as file:
        file.write(data + '\n')
        file.close()

def append():
    with open('data.txt', 'a') as file:
        file.write(data2 + '\n')
        file.close

def read():
    with open('data.txt', 'r') as file:
        return file.read()
        
write()
append()
read()
print(read())
"""

data3 = " Hello blah  blah blah "

def write2():
    with open('file.txt', 'w') as file:
        file.write(data3 + '\n')

write2()

def writer(file, data):
    with open(file, 'a') as file:
        file.write('\n' + data)

writer('file.txt', "some bunch of stuff")
