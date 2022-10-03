strings = ["car","moon","testing","torch","fly"]
numbers = [5,6,7,8,1,2,3]

def reverse(lis):
    lis.reverse()
    print(lis)

def join(first, second):
    new = first + second
    print(new)

def mult(lis):
    for x in lis:
    lis[x] =  x * x
    print(lis)

mult(numbers)
join(strings,numbers)
reverse(strings)
