import math
a = float(input("please enter num1: "))
print("choose what do you want to do: ")
print("1= +")
print("2= -")
print("3= *")
print("4= /")
print("5= Radical")
print("6= sin")
print("7= cot")
print("8= cos")
print("9= tan")
print("10= Factorial")
op = int(input("enter which one: "))
result = 0
if op == 1 :
    b = float(input("please enter num2: "))
    result = a + b
if op == 2 :
    b = float(input("please enter num2: "))
    result = a - b
if op == 3 :
    b = float(input("please enter num2: "))
    result = a * b
if op == 4 :
    b = float(input("please enter num2: "))
    if b != 0 :
        result = a / b
    else:
        result = "cannot divide by zero. "
if op == 5 :
    if a < 0 :
        result = "Radical does not exist for negative numbers. "
    else:
        result = math.sqrt(a)
if op == 6 :
    result = math.sin(math.radians(a))
if op == 7 :
    result = math.cos(math.radians(a)) / math.sin(math.radians(a))
if op == 8 :
    result = math.cos(math.radians(a))
if op == 9 :
    result = math.sin(math.radians(a)) / math.cos(math.radians(a))
if op == 10 :
    if a < 0 :
        result = "factorial does not exist for negative numbers. "
    else:
        result = math.factorial(a)
print(result)