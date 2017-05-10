import math

def numDivisors(n):
    div = 0
    counter = 1
    add = 0
    
    if n % 2 != 0:
        counter = 2
        pass
        
    end = math.sqrt(n)
    
    if n % end == 0:
        add = 1
    
    for i in xrange(1, int(math.ceil(end)), counter):
        if n%i == 0:
            div += 1
           
    return div * 2 + add
    
if __name__ == "__main__":
    old = 0
    total = 0
    
    for i in xrange(1, 10000000):
        if i%100000 == 0:
            print i
        new = numDivisors(i)
        
        if new == old:
            total += 1
            
        old = new

    print total