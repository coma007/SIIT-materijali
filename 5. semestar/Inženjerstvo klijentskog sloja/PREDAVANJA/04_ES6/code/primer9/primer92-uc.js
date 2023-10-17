var o = {
    x:1,
    m:function(){
      var f = () => {console.log(this)};
      f();
    }
}