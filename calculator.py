
def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2


print("***START***")
while True:
    num1 = int(input("Enter your number: "))
    print("1)add" + "2)subtract" + "3)multiply" + "4)divide" + "5)none")
    op = input("(1/2/3/4/5): ")
    if op == "5":
        print(num1)
        print("Done")
        break
    else:
        num2 = int(input("Enter your number: "))
        if op == "1":
            print("Result = ", addition(num1,num2))
        elif op == "2":
            print("Result =", subtraction(num1,num2))
        elif op == "3":
            print("Result =" , multiplication(num1,num2))
        elif op == "4":
            if num2!= 0:
                print("Result= ", divide(num1,num2))
            else:
                print("not defined")
        print("Do you want to continue? 1)yes  2)no")
        x = input("(1/2):")
        if x == "2":
            break
        if x == "1":
            pass