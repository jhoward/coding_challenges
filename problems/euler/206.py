import random

def isCorrect(number):
    
    t = number / 1000000000000000000
    if t < 1:
        return -1
    if t > 1:
        return 1
    
    t = (number / 10000000000000000) % 10
    if t < 2:
        return -1
    if t > 2:
        return 1
    
    t = (number / 100000000000000) % 10
    if t < 3:
        return -1
    if t > 3:
        return 1
    
    t = (number / 1000000000000) % 10
    if t < 4:
        return -1
    if t > 4:
        return 1
    
    t = (number / 10000000000) % 10
    if t < 5:
        return -1
    if t > 5:
        return 1

    t = (number / 100000000) % 10

    if t < 6:
        return -1
    if t > 6:
        return 1
    
    t = (number / 1000000) % 10
    if t < 7:
        return -1
    if t > 7:
        return 1
    
    t = (number / 10000) % 10
    if t < 8:
        return -1
    if t > 8:
        return 1
    
    t = number / 100
    if t < 9:
        return -1

    t = number % 10
    if t > 0:
        return 1

    return 0
    

cs = 0
cb = int(random.random() * 100000000000) + 100000000000
attempt = 0
oldNum = 0
while True:

    num = (cb + cs) / 2
    ns = num**2
    attempt += 1
    print "Attempt:" + str(attempt) + "   " + str(num) + "   " + str(ns)
    val = isCorrect(ns)
    if val == 0:
        break
    if val == 1:
        cb = num

    if val == -1:
        cs = num
    
    if oldNum == num:
        cs = 0
        cb = int(random.random() * 100000000000) + 100000000000
    
    oldNum = num    
