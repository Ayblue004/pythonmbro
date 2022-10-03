def minCov(min):
    print(min * 60)
def add(a,b):
    print(a + b)
def ageCov(years):
    print(years * 365)
def tempCov(temp):
    temp1 = temp - 32
    print(temp1 / 1.8)
minCov(2)
add(1,2)
ageCov(3)
tempCov(100)


words = ["a","me", "you", "she", "her"]

def list_func():
    print(words[0])
    print(words[len(words) - 1])
    words.sort()
    print(words)
    print(len(words))

list_func()
