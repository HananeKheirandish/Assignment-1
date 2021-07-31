weight = float(input("please enter your weight in kg: "))
height = float(input("please enter your height in m: "))
BMI = round(weight / height ** 2 , 2)

if BMI < 18.5 :
    print("Your BMI is ", BMI , "your body mass index is UNDERWEIGHT. ")
if 18.5 <= BMI < 25 :
    print("Your BMI is ", BMI , "your body mass index is NORMAL. ")
if 25 <= BMI < 30 :
    print("Your BMI is ", BMI , "your body mass index is OVERWEIGHT. ")
if 30 <= BMI < 35 :
    print("Your BMI is ", BMI , "your body mass index is OBESE. ")
if BMI >= 35  :
    print("Your BMI is ", BMI , " and your body mass index is EXTREMELY OBESE. ")