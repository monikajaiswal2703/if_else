num1 = int(input("enter the 1st no.:-"))
num2 = int (input("enter the 2 nd no.:-"))
num3 = int (input("enter the 3rd no.:-"))
if num1>num2 and num1>num3:
    print("num1 is greater", num1)
    if num2>num3:
        print("num2 is second greater", num2)
    else:
        print("num3 is second greater",num3)
elif num2>num1 and num2>num3:
    print("num2 is greater",num2)
    if num3>num1:
        print("num3 is second greater", num3)
    else:
        print("num1 is second greater",num1) 
elif num3>num2 and num3>num1:
    print("num3 is greater",num3)
    if num2>num1:
        print("num2 is second greater",num2)
    else:
        print("num1 is second greater",num1) 
else:
    print("error")                         

