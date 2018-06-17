var a = 97;
var charArray = {};
for (var i = 0; i<26; i++)
    charArray[String.fromCharCode(a + i)] = String.fromCharCode(a + i);

console.log(charArray);