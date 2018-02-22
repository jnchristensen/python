#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

dict1= {'0': 0, '1' : 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9':4 };
dict2= {'2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9':6 };
teens= {'0': 3, '1' : 6, '2': 6, '3': 8, '4': 8, '5': 7, '6': 7, '7': 9, '8': 8, '9':8 };
cnt = 0;

for i in range(1, 1001):
    num = str(i);
    if len(num) == 3:
        a = num[1];
        b = num[2];
        #if the number is not just a straight hundred
        if num[1] != "0" or num[2] != "0":
            # hundred and = 10 letters
            cnt += 10;
            #add the number of letters of the first digit
            cnt += dict1[num[0]];
            #if the second digit is 1
            if num[1] == "1":
                cnt += teens[num[2]];

            elif num[1] != "0":
                cnt+= dict2[num[1]];

            #add the letters for the third digit
            if num[1] != '1':
                cnt += dict1[num[2]];

        #add the count for the numbers that are just a straight hundred
        else:
            a = dict1[num[0]];
            b = num[0]
            cnt += dict1[num[0]] + 7;

    #count the 2 digit numbers
    elif len(num) == 2:
        #if the number is 10-19
        if num[0] == "1":
            cnt += teens[num[1]];
        else:
            cnt += dict2[num[0]];
            cnt += dict1[num[1]];
    #count for 1000
    elif len(num) == 4:
        cnt += 11;

    #count 1-9
    else:
        cnt += dict1[num[0]];

print(cnt);