import cProfile
import profile
import math

maxNum = 12

def numDigits(num):
    return int(math.log(num, 10)) + 1

def isReversible(number):
    
    if number % 10 == 0:
        return False
        
    dig = numDigits(number)
    
    if dig < 2:
        return False
    
    total = 0
    
    for i in range(dig):
        high = number / (10**(dig - 1 - i))
        low = number % (10**(i + 1))
        low = low / (10**i) 
        
        print high
        print low
        
        total = total * 10 + (high + low)
        
    print "--" + str(number) + " " + str(total)
    
    return subA(total)
    

def subA(number):
    
    while (number > 0):
        if number % 2 == 0:
            return False
        number = number / 10
        
    return True


def main():
    num = 0
    numReversible = 0
    i = 11
    while i < maxNum:
        num += 1
    
        if isReversible(i):
            print i
            numReversible += 1
        
        i += 1
        
    print numReversible


if __name__ == "__main__":
    profile.run('main()')
    #main()

