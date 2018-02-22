#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

# a = the number we want to find the largest prime factor for
a = 600851475143;

# b is our starting point to find the factors
b=2;

while a != 1:
    if a%b == 0:
        gcf = b;
        a = a/b;
        b = 2;
    else:
        b = b + 1;

print(gcf);