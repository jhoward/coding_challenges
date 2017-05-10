#Problem 301

count = 0

for i in xrange(1, 2**30 + 1):
	if i % 1000 == 0:
		print i
	heaps = (i, 2*i, 3*i)
	x = reduce(lambda x, y:x^y, heaps)

	if x == 0:
		count += 1

print count