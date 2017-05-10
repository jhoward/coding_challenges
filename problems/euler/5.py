start = 19*17*13*11*7*5*3
num = start

def check(num, limit = 20):

    for i in range(2, limit):
        if num%i != 0:
            return False
    return True
    
attempts = 0

while True:
    print num
    attempts += 1
    if check(num, 20):
        break
    num += start
    
print attempts




    
