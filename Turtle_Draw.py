import random
import numpy
import turtle 

x = "Cool" #Global Variables
def myfunc():
    y = ["A", "B", "C"] #Local Variables
    print("Python is " + x)

    # **python for loop**
    # Ex(1)
    # for i in y:
    #     print("y: "+i)
    # Ex(2)
    print("Start loop.. .")
    for i in range(2, 5):
        print(i)
    else:
        print("Loop finished!")

def draw():
    tt = turtle
    tt.speed(1000)
    tt.bgcolor('black')
    colors = ['blue','green','red','orange','purple','yellow','pink','lightblue','white']
    for i in range(1000):
        tt.pencolor(random.choice(colors))
        x = float(random.randint(-200,200))
        y = float(random.randint(-200,200))
        tt.goto(x,y)
        sideLength = i*2
        for x in range(random.randint(5,20)):
            tt.forward(sideLength)
            tt.left(123)

    tt.showturtle()
    tt.getscreen().mainloop()

# calculator
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multi(x,y):
    return x * y
def divide(x,y):
    return x / y

def calculator():

    while True:
        print("Select operation.")
        print("1.Add +")
        print("2.Subtract -")
        print("3.Multiply *")
        print("4.Divide /")
        # take input from the user
        choice = input("Enter choice number (1/2/3/4)")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multi(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid Input")
            next_calculation = input("Let's do calculation? (yes/no): ")
            if next_calculation == "no":
                break

def printMyName():
    fname = input('Enter your first name : ')
    lname = input('Enter your last name : ')
    age = input('Enter your age : ')
    print('Name : ' + fname +' '+ lname + ', Age : ' + age)

draw()