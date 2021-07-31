Firstname = input("please enter Firstname: ")
Lastname = input("please enter Lastname: ")
less1 = float(input("please enter mark of less1: "))
less2 = float(input("please enter mark of less2: "))
less3 = float(input("please enter mark of less3: "))
avg = round((less1 + less2 + less3)/3 , 2)
if(avg >= 17):
    print(Firstname , Lastname , "Your average is " , avg , " and your status is Great. ")
if(17 > avg >= 12):
    print(Firstname , Lastname , "Your average is " , avg , " and your status is Normal. ")
if(avg <= 12):
    print(Firstname , Lastname , "Your average is " , avg , " and your status is Fail.")