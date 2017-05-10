import math

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    
    # The running integer that's checked for primeness
    
    d = {}
    q = 2    
    
    while True:
        if q not in d:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            d[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1

        
def all_primes(stop):
    """Returns a list of all primes from 1 until the current number
    """
    primes = []
    a = gen_primes()
    cp = a.next()    

    while(cp < stop):
        primes.append(cp)
        cp = a.next()
        
    return primes


def is_prime(number):
    """Determines if a single number is prime or not.
    """
    if(number <= 1):
        return False

    if(number == 2):
        return True

    a = int(math.sqrt(number))+1
    divisor = 3

    if((number % 2) == 0):
        return False

    while(divisor < a):
        if((number % divisor) == 0):
            return False
        divisor += 2
    return True



def prime_sieve(limit):
    """Deprecated.  Found online this implementation of the famous prime sieve.

    I applogize to the original author for lack of credit.
    """
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
