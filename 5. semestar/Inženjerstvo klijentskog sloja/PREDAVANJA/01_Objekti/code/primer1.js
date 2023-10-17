//JavaScript objekti

//literal
var peraPeric = {
  "ime": "Pera",
  "prezime": "Peric",
  "godina studija": 3,
  "polozeni ispiti": [{
    "naziv": "Web programiranje",
    "ocena": 9
  }, {
    "naziv": "Arhitektura racunara",
    "ocena": 10
  }]
};

//pristup vrednostima svojstava
var x = peraPeric.ime;
console.log("ime: "+x);
x = peraPeric["polozeni ispiti"][0].naziv;
console.log("polozeni ispit: "+x);
x = peraPeric.brojIndeksa;
console.log("nepostojece svojstvo: "+x);
//x = peraPeric.brojIndeksa.master;
//console.log("svojstvo undefined objekta: "+x);

//izmena vrednosti svojstva
peraPeric["godina studija"]=4;
console.log("izmenjena vrednost godine studija: "+peraPeric["godina studija"]);
//brisanje svojstva
delete peraPeric["godina studina"]
console.log("nakon sto je izbrisana vrednost: "+peraPeric["godina studina"]);

//pristup po referenci
x = peraPeric["polozeni ispiti"];
x.push({"naziv":"Matematicka analiza 1", "ocena":8});
console.log("polozeni ispiti: " + JSON.stringify(peraPeric["polozeni ispiti"]));
