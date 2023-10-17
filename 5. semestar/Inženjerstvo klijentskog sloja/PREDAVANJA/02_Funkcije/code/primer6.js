//opseg vidljivosti varijabli
var f = function () {
  console.log(x);
  var x;
  console.log(x);
  x = 5;
  console.log(x);
};

//iskljucujemo upozorenje da nije neophodno inicijalizovati varijablu na undefined
/*jshint -W080 */
var f1 = function () {
  var x = undefined;
  console.log(x);
  x = 5;
  console.log(x);
};


f();
f1();
