import math

primeList = [2]

def isPrime(number):
    sN = int(math.sqrt(number)) + 1
    for n in primeList:
        if n > sN:
            return True
        if number % n == 0:
            return False
    return True


num = 3

while True:

    if isPrime(num):
        primeList.append(num)
        print num
    num += 2
    
    if num >= 2000000:
        break
        
print sum(primeList)