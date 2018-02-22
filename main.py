#Goldbach's conjecture - Every even integer greater than 2 can be represented by the sum of 2 prime numbers.
#Find which pairs of prime numbers when added equal the user input even integer

while True:
    try:
        x = int(input('enter an even integer greater than 2: '))
        if x == 2:
            print('Value must be greater than 2!')
        elif x%2 != 0:
            print('Must enter an even integer!')
        else:
            break
    except ValueError:
        print ("Input must be a number")


prime_array = []

#find primes under the input and store them in an array
for i in range(2, x):
    isprime= True
    for j in range(2, i-1):
        if i % j == 0:
            isprime= False
    if isprime:
        prime_array.append(i)

i = 0
goldbach_numbers1 = []
goldbach_numbers2 = []

#find the sum of 2 prime numbers that equal the even integer input
for k in prime_array:
    for i in prime_array:
        if i + k == x:
            goldbach_numbers1.append(i)
            goldbach_numbers2.append(k)

for c1, c2 in zip(goldbach_numbers1, goldbach_numbers2):
    print ("%-9s %s" % (c1, c2))
