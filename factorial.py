#This program returns the factorial of an input



x = int(input('Enter a number you would like to see the factorial for: '))

fac = 1
fac_array = []
ans = 0

for i in range(1,x + 1):
    fac = fac * i
    fac_array.append(fac)

#1/n! + 1/(n-1)!....
for n in fac_array:
    ans = 1/n + ans

print(fac)
print (ans)