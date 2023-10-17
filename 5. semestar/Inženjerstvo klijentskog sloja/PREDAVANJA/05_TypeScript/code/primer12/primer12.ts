class Motorbike{
    noOfWheels: number = 2;
    startEngine(){
        console.log('Brm brm');
    }
    ride(){
        this.startEngine();
        console.log('Brrrrrrm');
    }
}

class Car{
    noOfWheels: number = 4;
    noOfDoors: number = 4;
    startEngine(){
        console.log('Brm brm');
    }
    drive(){
        console.log('Off we go');
    }
}

function getVehicle(): Motorbike|Car {
    return new Motorbike;
}

let vehicle: Motorbike|Car = getVehicle();

vehicle.startEngine();
//  Property 'ride' does not exist on type 'Car'.
// vehicle.ride();
(vehicle as Motorbike).ride();
// (vehicle as Car).drive();

function isCar(vehicle: Motorbike|Car): vehicle is Car{
    return (vehicle as Car).drive !== undefined;
}

if(isCar(vehicle)){
    vehicle.drive();
}
else{
    vehicle.ride();
}