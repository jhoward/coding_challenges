def calcMin(d):
    y = 1
    v = d**0.5
    
    while True:
        #print "-----",y
        x = int(y*v) + 1
        if x**2 - d*(y**2) == 1:
            return x, y
        
        if y > 10000000:
            return 0, 0
        y += 1
            
big = (0, 0)
bigd = 2
d = 2

"""
def calcActual(d):
    for y in range(1, 100000):
        for x in range(y, 1000000):
            if x**2 - d*(y**2) == 1:
                return x, y
"""

while d <= 1000:
    
    print d
    
    tmp = calcMin(d)
    
    if tmp[0] > big[0]:
        big = tmp
        bigd = d
    
    d += 1
    
    tmp = d**0.5
    
    if int(tmp) == tmp:
        d += 1
        
print big
print bigd
                