list=8, 2, 3, -1, 7
def Multiplication(list):
    p=1
    for x in list:
        p*=x
    return p
print(Multiplication(list))