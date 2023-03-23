def addition(x, y):  # adding two numbers
    add = x + y
    return add


def subtraction(x, y):  # subtracting two numbers
    sub = x - y
    return sub


def multiplication(x, y):  # multiplication of two numbers
    multi = x * y
    return multi


def division(x, y):  # division of two numbers
    div = x / y
    return div


# main program
num1 = int(input("Enter First number:"))  # input1
num2 = int(input("Enter Second number:"))  # input2
op = input('''
A ----- ADD 
S ----- SUB
M ----- MULTI
D ----- DIV
Enter operation : ''')
# operators for choosing
if op == 'A':
    print(f'Addition of numbers {num1} and {num2} is {addition(num1, num2)}')
elif op == 'S':
    print(f'Subtraction of numbers {num1} and {num2} is {subtraction(num1, num2)}')
elif op == 'M':
    print(f'Multiplication of numbers {num1} and {num2} is {multiplication(num1, num2)}')
elif op == 'D':
    print(f'Division of numbers {num1} and {num2} is {division(num1, num2)}')
else:
    print("Enter correct operator")