var foo = 42;
var baz = function () {
	return 'first value';
};
export default { foo };
export var bar = "hello world";
export {baz};
//obzirom da se eksportuje BINDING objekta
//a ne vrednost objekta,
//kasnije izmene (bez obzira odakle se vrse)
//ODRAZICE SE na importovane vrednost
foo = 10; 
bar = "cool";
baz = function () {
	return 'second value';
};