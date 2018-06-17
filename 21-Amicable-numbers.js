// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(i) = a and d(a) = i, where i ≠ a, then i and a are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.

var sum = 0;

for (var i=1;i<10000;i++){
    var a = divisorSum(i);
    var b = divisorSum(a);
    
    if(b==i && i!=a){
        console.log("a:",a,"b:",b);
        sum += a;
    }
}

console.log("sum:",sum);

function divisorSum (n){
    let arr = [1];

    //we only need to go to sqrt(n) to find all the divisors
    for(var i = 2; i < Math.floor(n**.5)+1;i++){
        if(n%i==0){
            //add both divisors at once
            arr.push(i,n/i);
        }
    }

    // console.log(arr);

    return arr.reduce(function(acc,curr){
        return acc + curr;
    });
}

// console.log(divisorSum(220));