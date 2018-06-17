// You are given the following information, but you may prefer to do some research for yourself.

// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

//If total days % 7 then its a Sunday
var totalDays = 0;
var count = 0;
var year = 1901;

var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function countSundays(totalDays, year) {

    //add a day to Feb if it's a leap year
    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
        daysInMonth[2] += 1;
    }
    for (var i = 0; i < daysInMonth.length; i++) {
        if (totalDays % 7 == 0){
            count++
        }
        totalDays += daysInMonth[i];
    }

    //remove day from Feb
    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
        daysInMonth[2] -= 1;
    }

    if (year < 2000){
        year++;
        countSundays(totalDays, year);
    }
    else {
        console.log(count);
    }
}

countSundays(totalDays,year);