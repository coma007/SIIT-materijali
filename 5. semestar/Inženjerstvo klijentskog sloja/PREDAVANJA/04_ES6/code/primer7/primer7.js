'use strict';

var x = 1,
    y = 2,
    o = {
	x: x,
	y: y,
	show: function show() {
		console.log('x:', this.x, ',y:', this.y);
	}
};
o.show();
