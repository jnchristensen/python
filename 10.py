#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import math;

def isPrime(x) :
    if x == 1:
        return False;
    elif x == 2 or x == 3: # 2 and 3 are prime
        return True;
    elif x%2 == 0:
        return False;
    elif x < 9: # 4 6 and 8 were excluded by previous statements
        return True;
    elif x%3 == 0:
        return False;
    else:
        r = math.floor(x**.5)
        f = 5; # all primes greater than 3 can be written in the form 6k+/-1
        while f <= r:
            if x%f == 0:
                return False;
                break;
            if x%(f+2) == 0:
                return False;
                break;
            f = f + 6;
        return True;

limit = 2000000;
count = 1; #since we know that 2 is prime and we are going to go through all the odds
i = 1; #start on an odd and increment by 2 in the loop
sum = 2; #since we skipped 2 as a prime
prime = 0;

while i < limit:
    i = i + 2;
    if isPrime(i):
        prime = i;
        sum = sum + prime;
        count = count + 1;

print(sum);