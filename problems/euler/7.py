primeList = [2]

def isPrime(number):
    for n in primeList:
        if number % n == 0:
            return False
    return True


num = 3

while True:

    if isPrime(num):
        primeList.append(num)
        print num
    num += 2
    
    if len(primeList) == 10001:
        break
        
print primeList[-1]