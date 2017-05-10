def next(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1
        
def chain(start):
    
    n = start
    cl = 0
    
    while n != 1:
        n = next(n)
        cl += 1
    return cl
    

lv = 0
ln = 0
    
for i in xrange(1, 1000000):
    v = chain(i)
    
    if v > lv:
        lv = v
        ln = i
        
print ln
print lv
    