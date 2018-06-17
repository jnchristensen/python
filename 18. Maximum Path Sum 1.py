#By starting at the top of the triangle below and moving to adjacent numbers on the
#  row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom of the triangle in the file "18. triangle.txt"

file = open("18. triangle.txt", 'r');
array = [];

#parse through the file and split the rows
for i in file:
    #split i by spaces and append it to an array
    array.append(i.split(" "));

print (array)
