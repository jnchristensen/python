var fs = require('fs');

//load the file with the triangle and store it as an array
var testing = fs.readFile('/Users/joshuac/repos/proj-euler/18.\ triangle.txt', 'utf8', function (err, data) {
    var triangle = data.split("\n");
    for (let i = 0; i < triangle.length; i++) {
        triangle[i] = triangle[i].split(" ");
    }
    
    //transform the triangle to be all in integers
    for (var i =0; i<triangle.length;i++){
        for(var j= 0; j<triangle[i].length;j++){
            triangle[i][j] = parseInt(triangle[i][j]);
        }
    }
    
    FindMaxPath(triangle);
});

function FindMaxPath(triangle) {
    //start at the second to last row and add the larger number from the row below
    for (var j = triangle.length - 2; j > 0; j--) {
        for (var k = 0; k < triangle[j].length; k++) {
            if (triangle[j + 1][k] > triangle[j+1][k + 1]) {
                triangle[j][k] = parseInt(triangle[j + 1][k]) + parseInt(triangle[j][k]);
            }
            else {
                triangle[j][k] = parseInt(triangle[j + 1][k + 1]) + parseInt(triangle[j][k]);
            }
        }
    }
    triangle[1].sort();
    console.log(parseInt(triangle[1][1]) + parseInt(triangle[0]));
}