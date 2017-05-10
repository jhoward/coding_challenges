"""
Wanted to use observation that num rect is n*(n + 1)/2 for a given line but didn't immediately see 
how.  Now I do.  Should have applied that again to the other diemnsion.
"""
import math

def numRectangles(w, h):
    total = 0
    
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            total += (w - i + 1) * (h - j + 1)
            
    return int(total)


def dumbSearch(target = 100):

    maxDim = int(math.ceil((math.sqrt( 8 * target + 1) - 1) / 2.0))

    dist = target
    closestW = 1
    closestH = 1

    for i in range(1, maxDim + 1):
        for j in range(1, maxDim + 1):
            
            tmp = numRectangles(i, j)
            
            if abs(tmp - target) < dist:
                dist = abs(tmp - target)
                closestW = i
                closestH = j
            
            if tmp > target:
                break
    
    return (dist, closestW, closestH)


if __name__ == "__main__":
    print dumbSearch(2000000)