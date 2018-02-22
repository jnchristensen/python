#A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
ans = 0;

for i in range (101,999):
    for n in range (101,999):
        palin = i * n;
        palin = str(palin);

        # check if the first half of the string is equal to the second half backwards (with a step of -1)
        if palin[0:3] == palin[6:2:-1]:
            if int(palin) > ans:
                ans = int(palin);

print(ans);