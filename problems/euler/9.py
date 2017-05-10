def calcTrip(a, b):
    c = (a**2 + b**2)**0.5
    return c




if __name__ == "__main__":
    
    a = 1
    b = 1
    
    while True:
        c = calcTrip(a, b)
        ans = a + b + c
        print str(a) + "  " + str(b) + "  " + str(ans)

        if ans == 1000:
            break
        
        if ans > 1000:
            a += 1
            b = a - 1
        
        b = b + 1
        
    print str(a * b * calcTrip(a, b))

    