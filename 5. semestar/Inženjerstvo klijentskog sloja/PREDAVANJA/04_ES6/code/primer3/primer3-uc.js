var funcs = [];
for (let i = 0; i < 5; i++) {
	funcs.push( function(){
		console.log( 'let: ', i );
	} );
}
funcs[3](); // 3

//----------------------------------

var funcs1 = [];
for (var i1 = 0; i1 < 5; i1++) {
	funcs1.push( function(){
		console.log( 'var: ', i1 );
	} );
}
funcs1[3](); // 5
