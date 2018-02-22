#What is the value of the first triangle number to have over
# five hundred divisors?

#important note is that the nth triangle number can be representent by n*(n+1)/2

import math;

tri_number = 1;
div_count = 0;
i = 2;

while div_count < 500:
    div_count = 0;
    tri_number = tri_number + i;
    i = i + 1;

    #take the square root of the tri_number and loop that because after the square root everything repeats.
    for n in range(1,int(math.ceil(tri_number**.5)) + 1):
        if tri_number%n == 0:
            div_count += 2;
        #if it is a perfect square then the number of factors only increases by one on that check
        if n*n == tri_number:
            div_count -= 1;

    print(div_count);

print(tri_number)