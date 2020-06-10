#!/usr/bin/python3

import math

# for any given x, give a number of proper fractions n/x, so that they have no common divisor
# and 0<n/x<1


def get_divisors(x):
  result = set()
  for i in range(2,int(math.ceil(math.sqrt(x))+1)):
    if (x%i==0): #divisable
      result.add(i)
      while(x%i==0 and x>1):
        x = int(x/i) # we divide x by i as long as we can do it
      if (x>i): # there may be other divisitors
        result.update(get_divisors(x)) # get the opposite delimiter's parts as long as it is not simple and add it's result to ours
      return result
  else:
    return set([x])


def proper_fractions(n):
  n = n
  divisors = get_divisors(n)
  for divisor in divisors:
    n -= n/divisor
  return n

print (proper_fractions(25))
print (proper_fractions(628030483))
print (proper_fractions(7052326663  ))
