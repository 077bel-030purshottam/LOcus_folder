

def hcf(num1,num2):

    a = num1
    b = num2
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


print(hcf(12,18))
