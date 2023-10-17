(function () {
	var a = 2;

	{
			console.log(3+5)
			let a = 3;
			console.log( a ); // 3
	}

	console.log( a ); // 2

	//let i for petlja
	var funcs = [];
	for (let i = 0; i < 5; i++) {
	  funcs.push( function(){
	    console.log( 'let: ', i );
	  } );
	}
	funcs[3](); // 3 

}());
