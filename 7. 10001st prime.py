#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

#What is the 10,001st prime number?
i = 2;
isprime = True;
count = 0;
prime = int;

while count < 10001:
    isprime = True;
    if i != 2 and i % 2 == 0:
        isprime = False;
    else:
        for n in range(2,round(i**.5 + .5)):
            if i%n ==0:
                isprime = False;
                break;
    if isprime == True:
        prime = i;
        count = count + 1;
        print(count);
    i = i + 1;

print(prime);