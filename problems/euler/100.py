"""
This can simplify down to a pell equation of the form.
2(b-1/2)^2 - (n-1/2)^2 - 1/4 = 0
using b-1/2 = v/2 and n-1/2 = u/2 this yields
2v^2/4 - u^2/4 - 1/4 = 0
=> 2v^2 - u^2 = 1
"""

b = 493
n = 697
while n < 10**12:
  b, n = 3*b + 2*n - 2, 4*b + 3*n - 3

print b
print n
