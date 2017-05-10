import math

a = math.factorial(100)

a = str(a)
tmp = 0

for i in a:
    tmp += int(i)

print tmp
