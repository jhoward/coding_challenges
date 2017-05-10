"""prime_test.py

Test various implmentations of prime computation
"""

from euler import euler
import time

totalprimes = 1000000;

start = time.time()
euler.all_primes(totalprimes)
end = time.time()

print "Total time for allprimes:" + str(end - start)

start = time.time()
euler.prime_sieve(totalprimes)
end = time.time()

print "Total time for prime_sieve:" + str(end - start)
