num1=int(input("enter 1st no"))
num2=int(input("enter 2nd no"))
num3=int(input("enter 3rd no"))
def Max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("Greatest number:",num1)
    elif num2>num3 and num2>num3:
        print("Greatest number:",num2)
    else:
        print("Greatest number:",num3)
Max(num1,num2,num3)