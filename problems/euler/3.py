import math

number = 600851475143
maxNum = 0


def findPrimeFactor(number):
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i, number/i
    return None, number


while True:

    fac, newNum = findPrimeFactor(number)
    if fac == None:
        maxNum = max(newNum, maxNum)
        break
    else:
        maxNum = max(fac, maxNum)
        number = newNum
        
print maxNum
    