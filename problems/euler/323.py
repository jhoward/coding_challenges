#python 323.py  
#Author: James Howard
#Uses a bit of dynamic programming to solve the problem.
bits = 32
tries = 50
dp = {(0, 0) : 1}

#First create a function for nCk()
factorial = {0 : 1}
for i in range(1, 33):
    factorial[i] = factorial[i-1]*i

nCk = lambda n, k: factorial[n] // (factorial[k] * factorial[n - k])


def probDist(tries, flipped):
    #"""probabilty of having flipped bits flipped in tries attempts"""

    if (tries, flipped) in dp:
        return dp[(tries, flipped)]

    if tries == 0 and flipped > 0:
        return 0
    if tries > 0 and flipped == 0:
        return 0
    
    prob = 0

    #Finish this tomorrow
    for i in range(bits + 1):
        for partFlipped in range(max(0, i-b), min(i, bits-b)+1):
            prob += probDist(tries - 1, flipped - partFlipped) * (nCk()


"""
if __name__ == "__main__":
    out = 0
    for i in range(1, tries + 1):
        out += probDist(i, bits) * i
    print(out)
"""









factorial = {0:1}
for i in range(1, 33):
    factorial[i] = factorial[i-1] * i

bits = 2

comb = lambda n, k: factorial[n] // (factorial[k] * factorial[n-k])

dp = {
    (0, 0) : 1
}

def get_value(*args):
    if args in dp:
        return dp[args]
    
    length, rem = args
    if length > 0 and rem == 0:
        return 0
    if length == 0 and rem > 0:
        return 0
    result = 0
    for i in range(bits+1):
        for overlooked in range(max(0, i-rem), min(i, bits-rem)+1):
            result += get_value(length-1, rem-i+overlooked) * ((comb(bits-rem, overlooked) * comb(rem, i-overlooked) / (2 ** bits)))
    
    dp[args] = result
    return result

iters = 50

if __name__ == '__main__':
    result = 0
    for i in range(1, iters+1):
        result += get_value(i, bits) * i
    print("The result is:", result)
