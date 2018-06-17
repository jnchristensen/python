var fs = require('fs');
//build key
var a = 97;
var key = {};
for (var i = 0; i<26; i++){
    key[String.fromCharCode(a + i).toUpperCase()] = i + 1;
}

fs.readFile('/Users/joshuac/repos/proj-euler/22_names.txt', 'utf8', function (err, data) {
    var names = data.split(",");
    var ans = 0;
    names.sort();

    for (var i=0; i<names.length;i++){
       let sum = 0;
        for (var j=1;j<names[i].length-1;j++){
            sum += key[names[i][j]];
        }
        ans+=sum*(i+1);

    }

    console.log(ans);
});