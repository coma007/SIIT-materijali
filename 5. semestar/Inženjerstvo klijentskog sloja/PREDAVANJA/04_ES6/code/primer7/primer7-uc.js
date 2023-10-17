var x = 1, y = 2,
	o = {
		x, //x:x
		y, //y:y
		show(){ //show : function show(){ 
			console.log('x:',this.x,',y:',this.y);
		}
	}
	o.show();