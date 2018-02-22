#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# using the above sequence and ending once n = 1,
# Which starting number, under one million, produces the longest chain?

from time import time;

t = time();
n = 1;
g_cnt = 0;
dict = {};

while n < 1000000:
    cnt = 0;
    a = n;
    while a != 1:
        #check if the value is in the dictionary
        if a in dict:
            #add the current count to the count value in the dictionary
            cnt = cnt + dict[a];
            break;
        if a%2 == 0:
            a = a/2;
        else:
            a = 3*a + 1;
        cnt += 1;
    # add the value to the dictionary if it is not there
    if n not in dict:
        dict[n] = cnt;
    if cnt > g_cnt:
        g_cnt = cnt;
        ans = n;
    n += 1;

tt = time() - t;
print(ans);
print(tt);