//callback
function mySandwich(param1, param2, callback) {
    //alert je blokirajuca funkcija
    console.log('Started eating my sandwich.\n\nIt has: ' + param1 + ', ' + param2);
    //pozivamo callback funkciju
    callback();
}
//callback je neimenovana funkcija
mySandwich('ham', 'cheese', function() {
    console.log('Finished eating my sandwich.');
});
