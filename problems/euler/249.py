"""249.py

Author: James Howard

Use dynamic programming to compute all the combinations of primes to sum to a given number.

The idea is to continue to add a prime to the combinations of primes to get to a new 
combination sum (csum)
"""

from euler import euler

primes = euler.all_primes(5000)
csums = [1] + [0] * sum(primes)

total = 0
for p in primes:
	print "prime:" + str(p)
	total += p
	
	#Have to go from total to p or else you will get double counting.
	for t in range(total, p - 1, -1):
	#	print t
		csums[t] = csums[t] + csums[t - p]

	#print csums

count = 0

for p in range(2, total + 1):
	if euler.is_prime(p):
		count += csums[p] #% 10**16

print (count) % 10**16
