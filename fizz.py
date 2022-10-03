def fizz_buzz():
    x = range(50)
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz")
        elif i % 3 == 0:
            print("Buzz")
        elif i % 5 == 0:
            print ("FizzBuzz")

fizz_buzz()
