total = 0

def fib(oldVal, val, stop = 4000000):
    newVal = oldVal + val
    global total
    if newVal > stop:
        return newVal
    
    if newVal%2 == 0:
        total += newVal

    return fib(val, newVal, stop)

fib(0, 1, 4000001)
print total