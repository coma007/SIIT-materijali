const Person = function(name, height, weight) {
    this.name = name;
    this.height = height;
    this.weight = weight;
}

function countBMI(person) {
    return person.weight / person.height ** 2
}

const marko = new Person("jovan", 1.60, 60);
const jovan = new Person("marko", 2.00, 90);

console.log(marko.name + " " + countBMI(marko));
console.log(jovan.name + " " + countBMI(jovan));