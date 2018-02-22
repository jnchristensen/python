#What is the greatest product of four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in the 20×20 grid?

#open the file in read mode
grid = open("grid.txt", "r");
numbers = []

#append all the elements to a matrix called numbers
for i in grid:
    numbers.append(i.split());

ans = 0;

#Find the greatest value going left to right
for row in range(0,20):
    for col in range(0,16):
        sum = int(numbers[row][col]) * int(numbers[row][col+1]) * int(numbers[row][col+2]) * int(numbers[row][col+3]);
        if sum > ans:
            ans = sum;

#Find the greatest value going top to bottom
for col in range(0,20):
    for row in range(0,16):
        sum = int(numbers[row][col]) * int(numbers[row+1][col]) * int(numbers[row+2][col]) * int(numbers[row+3][col]);
        if sum > ans:
            ans = sum;

#Find the greatest value diagonally going right and down
for col in range(0,16):
    for row in range(0,16):
        sum = int(numbers[row][col]) * int(numbers[row+1][col+1]) * int(numbers[row+2][col+2]) * int(numbers[row+3][col+3]);
        if sum > ans:
            ans = sum;

#Find the greatest value diagonally going left and down
for col in range(3,20):
    for row in range(0,16):
        sum = int(numbers[row][col]) * int(numbers[row+1][col-1]) * int(numbers[row+2][col-2]) * int(numbers[row+3][col-3]);
        if sum > ans:
            ans = sum;

print(ans);