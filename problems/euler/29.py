num = {}

a = 101
b = 101

for i in range(2, a):
    for j in range(2, b):
        val = i ** j
        
        num[val] = 0
        
print len(num)