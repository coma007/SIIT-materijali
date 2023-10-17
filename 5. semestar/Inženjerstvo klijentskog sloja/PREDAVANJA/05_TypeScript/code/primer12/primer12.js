var Motorbike = /** @class */ (function () {
    function Motorbike() {
        this.noOfWheels = 2;
    }
    Motorbike.prototype.startEngine = function () {
        console.log('Brm brm');
    };
    Motorbike.prototype.ride = function () {
        this.startEngine();
        console.log('Brrrrrrm');
    };
    return Motorbike;
}());
var Car = /** @class */ (function () {
    function Car() {
        this.noOfWheels = 4;
        this.noOfDoors = 4;
    }
    Car.prototype.startEngine = function () {
        console.log('Brm brm');
    };
    Car.prototype.drive = function () {
        console.log('Off we go');
    };
    return Car;
}());
function getVehicle() {
    return new Motorbike;
}
var vehicle = getVehicle();
vehicle.startEngine();
//  Property 'ride' does not exist on type 'Car'.
vehicle.ride();
vehicle.drive();
function isCar(vehicle) {
    return vehicle.drive !== undefined;
}
if (isCar(vehicle)) {
    vehicle.drive();
}
else {
    vehicle.ride();
}
