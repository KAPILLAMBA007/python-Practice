input_set = {1, 2, 3, 4, 5}
s = 1
for item in input_set:
    for number in range(1,item+1):
        s= s * number
    print ("Factorial of", item, "is", s)