#As a Developer, I want to be able to find the even numbers between x and y inclusively

def find_even(x,y):
    for i in range(x,y):
        if i % 2 == 0:
            print(i)
x = int(input('x: '))
y = int(input('y: '))
find_even(x,y)