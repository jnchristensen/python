#2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.

#What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

loop = True;
n = 0;

while loop == True:
    loop = False;
    n = n + 20;
    for i in range (1,10):
        if n%i != 0:
            print(n);
            loop = True;
            break;

print(n);