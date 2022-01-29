//funkcija koja ocitava vrednost URL parametra sa prosledjenim imenom
function getParamValue(name) {
	var location = decodeURI(window.location.toString());
	var index = location.indexOf("?")+1;
	var subs = location.substring(index, location.length);
	var splitted = subs.split("&");

	for(i=0; i < splitted.length; i++) {
		var s = splitted[i].split("=");
		var pName  = s[0];
		var pValue = s[1];
		if(pName == name) {
			return pValue;
		}
	}	
}

let username = getParamValue("user");
let userSpan = document.getElementById("userSpan");
userSpan.innerText = username;