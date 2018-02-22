#What is the value of the first triangle number to have over
# five hundred divisors?

#important note is that the nth triangle number can be representent by n*(n+1)/2

import math;
from time import time;

def divisors(n):
    num_factors = 0;
    for i in range(1,int(math.ceil(n**.5))+1):
        if n%i == 0:
            num_factors += 2;
        # if it is a perfect square then subtract one factor
        if i*i == n:
            num_factors -= 1;
    return num_factors;

cnt = 0;
n = 1;
t = time();

while cnt < 500:
    Tn = (n*(n+1))/2;
    if n%2 == 0:
        cnt = divisors(n/2)*divisors(n+1);
    else:
        cnt = divisors(n)*divisors((n+1)/2);
    n += 1;

tt = time() - t;
print(Tn);
print(tt);