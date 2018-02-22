#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("13. file", "r");

sum = 0;

for i in f:
    sum += int(i);

sum = str(sum);

print(sum[:10]);