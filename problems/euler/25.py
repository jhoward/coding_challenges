import math

phi = (1 + math.sqrt(5))/2.0

def calcFibTerm(n):
    phiN = divmod(n * math.log10(phi), 1.0)
    print phiN
    phiN = (phiN[0], (10**phiN[1]) / math.sqrt(5))
    return phiN
    
print calcFibTerm(4781)