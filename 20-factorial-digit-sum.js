// n! means n × (n − 1) × ... × 3 × 2 × 1

// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

// Find the sum of the digits in the number 100!

var n = 100;
var fac = n;
var string = "";

for (var i = 1; i < n; i++) {
    fac *= i;
    var facString = fac.toString();

    while (facString[facString.length - 1] == 0) {
        console.log(fac);
        fac = parseInt(facString.slice(0, -1));
        facString = fac.toString();
    }
    console.log(facString, i);
}

var ans = facString.split("").reduce(function (accumulator, currentValue, currentIndex, array) {
    return parseInt(accumulator) + parseInt(currentValue);
});

console.log(ans);