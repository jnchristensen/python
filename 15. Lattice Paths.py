#Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.

#How many such routes are there through a 20×20 grid?

#Thoughts: we know we have to go 20 right and 20 down but it doesn't matter
#the order of it so the answer to this problem is 40 choose 20.
# 40 choose 20 = 40!/(20!*(40-20)!)

n = 40;
k = 20;
n_fact = 1;
k_fact = 1;
 
# this is 40!/(40-20)!
for i in range(n-k + 1,n + 1):
    n_fact *= i;

#this is just 20!
for m in range(1,1+k):
    k_fact *= m;


ans = n_fact/(k_fact);
print(ans);