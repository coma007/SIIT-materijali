var funcs = [];
for (let i = 0; i < 5; i++){
    funcs.push(function(){
        console.log('var i: ',i);
    });
}
funcs[3]();