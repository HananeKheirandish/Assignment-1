side1 = float(input("please enter side1: "))
side2 = float(input("please enter side2: "))
side3 = float(input("please enter side3: "))
A = (side2 + side3)
B = (side1 + side3)
C = (side1 + side2)
if A>side1 and B>side2 and C>side3 :
    print("You can make triangle. ")
else:
    print("You can't make triangle. ")